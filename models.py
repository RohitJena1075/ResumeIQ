# Not used in current login-free version
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(50))
    skills = db.Column(db.Text)
    education = db.Column(db.Text)
    experience = db.Column(db.Text)
    achievements = db.Column(db.Text)
    certifications = db.Column(db.Text)
    publications = db.Column(db.Text)
    volunteering = db.Column(db.Text)
    summary = db.Column(db.Text)
    score = db.Column(db.Float)
    job_keywords = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Resume {self.name}>"

    def to_dict(self):
        return {
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
            "Skills": self.skills,
            "Education": self.education,
            "Experience": self.experience,
            "Achievements": self.achievements,
            "Certifications": self.certifications,
            "Publications": self.publications,
            "Volunteering": self.volunteering,
            "Summary": self.summary,
            "Score": self.score,
            "JobKeywords": self.job_keywords,
            "CreatedAt": self.created_at.isoformat()
        }
