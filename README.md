🚀 SkillSwap – Skill Sharing & Chat Platform

A full-stack Flask web application that allows users to exchange skills, chat in real-time, and manage profiles. Built with modern development practices including Docker and GitHub integration.

📑 Table of Contents
Features
Project Structure
Tech Stack
Getting Started
Local Setup
Docker Setup
GitHub Setup
Application Flow
Future Improvements
✨ Features
Category	Features
Authentication	User registration & login system
Chat System	One-to-one messaging with file sharing
Skills	Add, view, and exchange skills
Dashboard	User dashboard with navigation
File Upload	Send files in chat
Message Status	Sent / Seen status
UI	Simple responsive interface
📁 Project Structure
SkillSwap/
│
├── app.py                 # Main Flask app
├── templates/             # HTML pages
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── chat.html
│   └── mychats.html
│
├── static/
│   ├── style.css
│   └── uploads/           # Uploaded files
│
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker config
├── .gitignore             # Ignore unnecessary files
└── README.md              # Project documentation
🛠️ Tech Stack
Category	Technology
Backend	Flask (Python)
Database	SQLite / SQLAlchemy
Frontend	HTML, CSS
File Handling	Werkzeug
Containerization	Docker
Version Control	Git & GitHub
⚙️ Getting Started
Prerequisites
Python 3.10+
pip
Git
(Optional) Docker
💻 Local Development
# Clone repo
git clone https://github.com/your-username/skillswap.git
cd skillswap

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py

👉 Open:
http://127.0.0.1:5000

🐳 Docker Setup
Build Image
docker build -t skillswap-app .
Run Container
docker run -p 5000:5000 skillswap-app

👉 Open:
http://localhost:5000

🔗 GitHub Setup (Step-by-step)
git init
git add .
git commit -m "Initial commit - SkillSwap project"

git branch -M main
git remote add origin https://github.com/your-username/skillswap.git
git push -u origin main
🔄 Application Flow
User registers / logs in
User enters dashboard
User selects another user
Chat starts
Messages stored in database
File uploads saved in /static/uploads
Message status updated (Sent → Seen)
💬 Chat Features
Send text messages
Upload files
Delete messages
Auto scroll to latest message
Status tracking

⚠️ Current limitation:

Chat does not auto-update (manual refresh needed)
🔮 Future Improvements
Real-time chat using WebSockets
Notifications
Profile pictures
Skill matching system
Group chat
Deploy on cloud (Render / AWS)
🛡️ Security Notes
Add password hashing (recommended: werkzeug.security)
Validate file uploads
Avoid storing plain passwords
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
SkillSwap Project

📄 License

This project is for academic and learning purposes.

🎯 Bonus (for your viva)

If they ask:

Why Docker?
👉 “To make my application portable and run consistently across different systems.”

Why GitHub?
👉 “For version control, collaboration, and project showcasing.”
