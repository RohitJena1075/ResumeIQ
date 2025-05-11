# parser/summary_generator.py
import os
import cohere
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_summary(text: str) -> str:
    if len(text.split()) < 30:
        return "Not enough content to summarize."

    try:
        response = co.chat(
            model="command-r",  # or "command"
            message=f"Summarize this resume in 5 bullet points:\n\n{text}"
        )
        return response.text.strip()
    except Exception as e:
        return f"Cohere API Error: {e}"



