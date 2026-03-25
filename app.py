import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.secret_key = "secretkey"

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://JTY\\SQLEXPRESS/SkillSwapDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# FILE UPLOAD
app.config['UPLOAD_FOLDER'] = 'static/uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

db = SQLAlchemy(app)

# MODELS
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    skill = db.Column(db.String(100))
    category = db.Column(db.String(100))
    description = db.Column(db.String(1000))

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100))
    receiver = db.Column(db.String(100))
    skill = db.Column(db.String(100))
    status = db.Column(db.String(20), default="Pending")

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100))
    receiver = db.Column(db.String(100))
    message = db.Column(db.String(1000))
    status = db.Column(db.String(20), default="Sent")
    file = db.Column(db.String(200))


# ROUTES
@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        new_user = User(
            username=username,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            username=request.form["username"],
            password=request.form["password"]
        ).first()

        if user:
            session["user"] = user.username
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    skills = Skill.query.filter_by(username=session["user"]).all()

    new_messages = db.session.query(func.count(Message.id)).filter(
        Message.receiver == session["user"],
        Message.status == "Sent"
    ).scalar()

    return render_template("dashboard.html",
        skills=skills,
        user=session["user"],
        new_messages=new_messages
    )


@app.route("/addskill", methods=["POST"])
def addskill():
    if "user" not in session:
        return redirect("/login")

    skill = Skill(
        username=session["user"],
        skill=request.form["skill"],
        category=request.form["category"],
        description=request.form["description"]
    )

    db.session.add(skill)
    db.session.commit()

    return redirect("/dashboard")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/explore", methods=["GET","POST"])
def explore():
    if request.method == "POST":
        search = request.form["search"]
        skills = Skill.query.filter(
            Skill.skill.contains(search) |
            Skill.category.contains(search) |
            Skill.username.contains(search)
        ).all()
    else:
        skills = Skill.query.all()

    return render_template("explore.html", skills=skills)


@app.route("/delete/<int:id>")
def delete(id):
    skill = Skill.query.get(id)
    db.session.delete(skill)
    db.session.commit()
    return redirect("/dashboard")


@app.route("/request/<username>/<skill>")
def request_skill(username, skill):
    req = Request(
        sender=session["user"],
        receiver=username,
        skill=skill
    )
    db.session.add(req)
    db.session.commit()
    return redirect("/explore")


@app.route("/requests")
def requests():
    all_requests = Request.query.filter(
        (Request.sender == session["user"]) |
        (Request.receiver == session["user"])
    ).all()

    return render_template("requests.html", requests=all_requests)


@app.route("/update_request/<int:id>/<action>")
def update_request(id, action):
    req = Request.query.get(id)

    if action == "accept":
        req.status = "Accepted"
    elif action == "reject":
        req.status = "Rejected"

    db.session.commit()
    return redirect("/requests")


# CHAT
@app.route("/chat/<username>", methods=["GET","POST"])
def chat(username):

    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        msg = request.form["message"]
        file = request.files.get("file")

        filename = None
        if file and file.filename != "":
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_msg = Message(
            sender=session["user"],
            receiver=username,
            message=msg,
            file=filename
        )

        db.session.add(new_msg)
        db.session.commit()

    # MARK AS SEEN
    Message.query.filter_by(
        receiver=session["user"],
        sender=username,
        status="Sent"
    ).update({"status": "Seen"})
    db.session.commit()

    messages = Message.query.filter(
        ((Message.sender == session["user"]) & (Message.receiver == username)) |
        ((Message.sender == username) & (Message.receiver == session["user"]))
    ).order_by(Message.id).all()

    return render_template("chat.html", messages=messages, username=username)


@app.route("/mychats")
def mychats():
    chats = db.session.query(Message.sender, Message.receiver).filter(
        (Message.sender == session["user"]) |
        (Message.receiver == session["user"])
    ).distinct().all()

    users = set()
    for c in chats:
        if c.sender != session["user"]:
            users.add(c.sender)
        if c.receiver != session["user"]:
            users.add(c.receiver)

    return render_template("mychats.html", users=users)

@app.route("/delete_message/<int:id>")
def delete_message(id):
    if "user" not in session:
        return redirect("/login")

    msg = Message.query.get(id)

    # only allow sender to delete
    if msg and msg.sender == session["user"]:
        db.session.delete(msg)
        db.session.commit()

    return redirect(request.referrer)

if __name__ == "__main__":
    app.run(debug=True)