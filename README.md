# ✨ SkillSync – NLP-Powered Resume Analyzer 🔥

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25-orange)
![GitHub Repo](https://img.shields.io/badge/GitHub-ResumeAnalyzer-green)

SkillSync is an **interactive web app** that analyzes resumes against job descriptions.  
It uses **Python and NLP techniques** to extract keywords, calculate match scores, and suggest missing skills — simulating an **AI-driven ATS system**.  

This project is perfect for students and job seekers to **see how well their resume matches a job description** and identify areas for improvement.  

---

## 📌 Features

- 📄 Upload resume (PDF)  
- 📝 Paste job description  
- 🚀 Get match score (%)  
- ⚠️ Highlight missing skills  
- 🎨 Interactive Streamlit interface  

---

## 🛠️ Tech Stack

- **Python** – backend logic  
- **Streamlit** – frontend interface  
- **PyPDF2, Regex, Counter** – keyword extraction  

---

## 📌 How It Works

1. Extract text from PDF resumes using **PyPDF2**  
2. Clean and tokenize text → remove special characters, lowercase, split words  
3. Extract top keywords from resume & job description  
4. Calculate match score (%)  
5. Show missing keywords to improve resume  

## 🌐 Live Demo

Try it live on **Streamlit Cloud** (deployed and fully functional):  
[🔗 Open SkillSync](https://resume-analyzer-tdmfarjvw3ef96zausbzkt.streamlit.app/)
