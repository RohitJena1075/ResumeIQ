# routes/core.py

import os, io, csv, collections
from flask import Blueprint, render_template, request, send_file
from parser.extractor import extract_details
from parser.pdf_reader import read_pdf
from parser.docx_reader import read_docx
from parser.summary_generator import generate_summary
from sentence_transformers import SentenceTransformer, util
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

core = Blueprint('core', __name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

parsed_resumes = []

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']
    keywords = request.form['keywords']
    if not file:
        return "No file uploaded.", 400

    filename = file.filename
    upload_dir = 'uploads'
    os.makedirs(upload_dir, exist_ok=True)
    filepath = os.path.join(upload_dir, filename)
    file.save(filepath)

    text = read_pdf(filepath) if filename.endswith('.pdf') else read_docx(filepath)
    data = extract_details(text)
    summary = generate_summary(text)

    resume_text = " ".join([
        ' '.join(data.get('Education', [])),
        ' '.join(data.get('Skills', [])),
        ' '.join(data.get('Experience', []))
    ])
    job_embedding = model.encode(keywords, convert_to_tensor=True)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(job_embedding, resume_embedding).item()

    data["Summary"] = summary
    data["Score"] = round(similarity, 4)
    data["JobKeywords"] = keywords
    parsed_resumes.append(data)

    return render_template("result.html", data=data)

@core.route('/dashboard')
def dashboard():
    skill_counter = collections.Counter()
    for r in parsed_resumes:
        for skill in r.get("Skills", []):
            skill_counter[skill] += 1

    chart_labels = list(skill_counter.keys())
    chart_values = list(skill_counter.values())
    return render_template("dashboard.html", resumes=parsed_resumes, chart_labels=chart_labels, chart_values=chart_values)

@core.route('/export/csv')
def export_csv():
    filepath = os.path.join('uploads', 'resumes.csv')
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Email', 'Phone', 'Skills', 'Score', 'Summary'])
        for r in parsed_resumes:
            writer.writerow([
                r['Name'], r['Email'], r['Phone'],
                ", ".join(r.get('Skills', [])),
                r.get('Score', ''),
                r.get('Summary', '').replace('\n', ' ')
            ])
    return send_file(filepath, as_attachment=True)

@core.route('/export/pdf')
def export_pdf():
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 50

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Resume Summaries Report")
    y -= 30
    p.setFont("Helvetica", 10)

    for r in parsed_resumes:
        if y < 100:
            p.showPage()
            y = height - 50
        p.drawString(50, y, f"{r['Name']} | {r['Email']} | Score: {r['Score']}")
        y -= 15
        p.setFont("Helvetica-Oblique", 9)
        summary = r.get('Summary', 'No summary available')
        for line in summary.splitlines():
            p.drawString(60, y, line.strip())
            y -= 12
        y -= 10
        p.setFont("Helvetica", 10)

    p.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="resume_summaries.pdf", mimetype='application/pdf')







