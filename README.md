
# 📄 Smart Resume Parser with AI Insights

A web app that lets you upload resumes, extract structured details, and analyze them using AI for skill matching, experience alignment, and job description relevance — all in a clean UI.

---

## 🚀 Features

- 📄 Upload PDF/DOCX resumes
- 🧠 NLP-powered resume parsing using spaCy
- 📊 Matching score based on job description
- 📝 AI-generated summary (optional lightweight logic)
- 📈 Dashboard with skill frequency chart
- 📤 Export data to CSV & PDF


---

## 🧰 Tech Stack

| Component | Technology         |
|----------|--------------------|
| Backend  | Flask              |
| NLP      | spaCy (`en_core_web_trf`) |
| Frontend | Bootstrap 5, Chart.js |
| Export   | ReportLab (PDF), CSV |
| Parsing  | PyPDF2, python-docx |


---

## 📦 Setup & Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-resume-parser.git
cd smart-resume-parser
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run the App

```bash
python run.py
```

Go to `http://127.0.0.1:5000` in your browser.

---

## 🧪 Sample Resume Upload Flow

1. Upload a PDF/DOCX resume
2. Paste a job description to compare
3. View extracted info + AI match score
4. See chart of detected skills
5. Visit dashboard for all parsed resumes

---

## 📁 Folder Structure

```
smart_resume_parser/
│
├── parser/                # Text extractors & NLP logic
│   ├── extractor.py
│   ├── pdf_reader.py
│   ├── docx_reader.py
│
├── routes/                # Flask route Blueprints
│   └── core.py
│
├── static/                # CSS, JS
│   └── style.css
│
├── templates/             # HTML templates
│   ├── index.html
│   ├── result.html
│   ├── dashboard.html
│
├── .env                   # Environment variables (if used)
├── app.py                 # App entry
├── config.py              # Configuration
├── models.py              # Data models
├── requirements.txt
├── run.py
```

---
