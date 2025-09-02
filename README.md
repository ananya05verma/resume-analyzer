SkillSync – NLP-Powered Resume Analyzer

SkillSync is an interactive web app that analyzes resumes against job descriptions.
It uses Python and basic NLP techniques to extract keywords, calculate match scores, and suggest missing skills — simulating an AI-driven ATS system.

📌 Features

📄 Upload resume (PDF)

📝 Paste job description

🚀 Get match score (%)

⚠️ Highlight missing skills

🎨 Interactive Streamlit interface

🛠️ Tech Stack

Python – backend logic

Streamlit – frontend interface

PyPDF2, Regex, Counter – keyword extraction

📌 How It Works

Extract text from PDF resumes using PyPDF2

Clean and tokenize text → remove special characters, lowercase, split words

Extract top keywords from resume & job description

Calculate match score (%)

Show missing keywords to improve resume

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py

🌐 Live Demo

Try it live on Streamlit Cloud:
🔗 Open SkillSync
