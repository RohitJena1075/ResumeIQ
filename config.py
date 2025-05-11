import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")

