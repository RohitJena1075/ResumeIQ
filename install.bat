@echo off
echo 🔧 Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

echo 📦 Installing dependencies...
pip install -r requirements.txt

echo 📥 Downloading spaCy transformer model...
python -m spacy download en_core_web_trf

echo ✅ Setup complete!
echo Run the app with:
echo   venv\Scripts\activate
echo   python run.py
pause
