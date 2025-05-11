import spacy
import re

# Load spaCy transformer-based English model
nlp = spacy.load("en_core_web_trf")

# A curated list of common tech and soft skills
SKILLS_DB = {
    'python', 'java', 'c++', 'sql', 'html', 'css', 'javascript',
    'machine learning', 'deep learning', 'pytorch', 'tensorflow',
    'flask', 'django', 'react', 'node.js', 'excel', 'communication',
    'leadership', 'problem solving', 'data analysis', 'git', 'linux'
}

def extract_details(text: str) -> dict:
    doc = nlp(text)

    # Extract name using PERSON entity
    name = next((ent.text for ent in doc.ents if ent.label_ == 'PERSON'), 'Not Found')

    # Extract email and phone using regex
    email = re.search(r"[\w\.-]+@[\w\.-]+", text)
    phone = re.search(r"\+?\d[\d\s\-]{7,}\d", text)

    # Extract skills by checking against known skills (case insensitive match)
    found_skills = set()
    for token in doc:
        token_text = token.text.lower()
        if token_text in SKILLS_DB:
            found_skills.add(token_text)

    # Extract education from entities (ORG or degree mentions)
    education = [
        ent.text for ent in doc.ents
        if ent.label_ in ['ORG', 'EDUCATION'] or 'university' in ent.text.lower()
    ]

    # Extract experience using keyword pattern
    experience = [
        sent.text.strip()
        for sent in doc.sents
        if re.search(r"\d+\+?\s?(years|yrs)", sent.text, re.IGNORECASE)
    ]

    return {
        'Name': name,
        'Email': email.group() if email else 'Not Found',
        'Phone': phone.group() if phone else 'Not Found',
        'Education': list(set(education)),
        'Skills': list(found_skills),
        'Experience': experience,
        'Achievements': [],
        'Certifications': [],
        'Publications': [],
        'Volunteering': []
    }

