# 🚀 SkillSwap – Skill Sharing & Chat Platform

A full-stack Flask web application that allows users to exchange skills, chat with each other, and share files. Built using Flask, SQLAlchemy, Docker, and GitHub.

---

## 📑 Table of Contents
- Features  
- Project Structure  
- Tech Stack  
- Getting Started  
- Local Setup  
- Docker Setup  
- GitHub Setup  
- Application Flow  
- Future Improvements  

---

## ✨ Features

| Category | Features |
|--------|---------|
| Authentication | User registration & login |
| Chat System | One-to-one messaging |
| Skills | Add and view skills |
| File Upload | Send files in chat |
| Dashboard | User dashboard |
| Message Status | Sent / Seen |

---

## 📁 Project Structure

SkillSwap/
│
├── app.py  
├── templates/  
│   ├── login.html  
│   ├── register.html  
│   ├── dashboard.html  
│   ├── chat.html  
│   └── mychats.html  
│
├── static/  
│   ├── style.css  
│   └── uploads/  
│
├── models.py  
├── requirements.txt  
├── Dockerfile  
├── .gitignore  
└── README.md  

---

## 🛠️ Tech Stack

- Backend: Flask (Python)  
- Database: SQLite / SQLAlchemy  
- Frontend: HTML, CSS  
- File Handling: Werkzeug  
- Containerization: Docker  
- Version Control: GitHub  

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.10+
- pip
- Git
- (Optional) Docker

---

## 💻 Local Development

```bash
git clone https://github.com/your-username/skillswap.git
cd skillswap

pip install -r requirements.txt
python app.py
Open in browser:
http://127.0.0.1:5000
🐳 Docker Setup
Build Image
docker build -t skillswap-app .
Run Container
docker run -p 5000:5000 skillswap-app
Open:
http://localhost:5000
🔗 GitHub Setup
git init
git add .
git commit -m "Initial commit - SkillSwap"

git branch -M main
git remote add origin https://github.com/your-username/skillswap.git
git push -u origin main
🔄 Application Flow
User registers or logs in
User enters dashboard
User selects another user
Chat starts
Messages saved in database
Files stored in static/uploads
Status updates (Sent → Seen)
💬 Chat Features
Send messages
Upload files
Delete messages
View message status

Note:
Chat currently requires manual refresh to update messages.

🔮 Future Improvements
Real-time chat (AJAX / WebSocket)
Profile pictures
Skill matching system
Notifications
Group chat
Cloud deployment
🛡️ Security Notes
Use password hashing (Werkzeug recommended)
Validate file uploads
Do not store plain passwords
📦 .gitignore Example
__pycache__/
*.pyc
.env
venv/
instance/
*.db
static/uploads/
❤️ Author

Jaity Rangtaina
BCA Analytics Student

📄 License

This project is for academic purposes.


---

If you want, I can also:
- make it **more advanced (like that JWT project)**  
- or add **screenshots section + badges + GitHub Actions**

Just tell me 👍
