SkillSync – NLP-Powered Resume Analyzer

SkillSync is an interactive web app that analyzes resumes against job descriptions.
It uses Python and basic NLP techniques to extract keywords, compute match scores, and suggest missing skills, simulating an AI-driven ATS system.

This project is perfect for students and job seekers to see how well their resume matches a job description and identify areas for improvement.

📌 Let’s Create a Resume Analyzer with Python

Python has a rich collection of libraries for text processing and web apps.
For SkillSync, we primarily use:

PyPDF2 → To extract text from PDF resumes

Streamlit → To create an interactive and eye-catching frontend

Both libraries can be installed using pip:

pip install PyPDF2
pip install streamlit

📌 Reading the PDF Resume

PyPDF2 allows us to read PDF files and extract text from each page.
It supports tasks such as:

Extracting text from PDF pages

Handling multiple pages

Manipulating PDF files (optional for future upgrades)

Example code to read a PDF:

import PyPDF2

pdf_reader = PyPDF2.PdfReader(open('resume.pdf', 'rb'))
resume_text = ""
for page in pdf_reader.pages:
    if page.extract_text():
        resume_text += page.extract_text()

📌 Extracting Keywords from Resume and Job Description

We use basic NLP techniques:

Convert text to lowercase

Remove special characters

Split text into words (tokenization)

Count the most common keywords using Counter

import re
from collections import Counter

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    return text.split()

def get_top_keywords(text, n=15):
    words = clean_text(text)
    counts = Counter(words)
    return [w for w, _ in counts.most_common(n)]

📌 Calculating Match Score

We compare keywords from the resume and job description to see how closely they match.
The match score is calculated as:

def match_score(resume_keywords, jd_keywords):
    matches = [w for w in jd_keywords if w in resume_keywords]
    if len(jd_keywords) == 0:
        return 0
    return round((len(matches) / len(jd_keywords)) * 100, 2)


✅ Higher score → Resume closely matches the job description

⚠️ Missing keywords are highlighted for improvement

📌 Interactive Streamlit Frontend

Streamlit allows creating a user-friendly web interface:

Upload your resume (PDF)

Paste a job description

Click “Start Analysis” → see match score and missing keywords

View extracted resume text (optional)

Example snippet:

import streamlit as st

resume_file = st.file_uploader("Upload Resume (PDF)")
job_description = st.text_area("Paste Job Description")

if st.button("🚀 Start Analysis"):
    # Run analysis here
    st.metric("Match Score", f"{score}%")

📌 Run the App Locally
pip install -r requirements.txt
streamlit run app.py