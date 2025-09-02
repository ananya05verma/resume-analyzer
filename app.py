import streamlit as st
import PyPDF2
import re
from collections import Counter


# Function to extract text from PDF

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# Function to clean text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text) 
    words = text.split()
    return words


# Function to extract keywords

def get_top_keywords(text, n=15):
    words = clean_text(text)
    counts = Counter(words)
    common = [w for w, _ in counts.most_common(n)]
    return common


# Function to Match Score

def match_score(resume_keywords, jd_keywords):
    matches = [w for w in jd_keywords if w in resume_keywords]
    if len(jd_keywords) == 0:
        return 0
    return round((len(matches) / len(jd_keywords)) * 100, 2)


# Streamlit UI

st.set_page_config(page_title="SkillSync", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
    .title {
        font-size:40px !important;
        color:#4CAF50;
        text-align:center;
        font-weight:bold;
    }
    .subtitle {
        font-size:20px;
        color:#555;
        text-align:center;
        margin-bottom:20px;
    }
    .keyword-box {
        display:inline-block;
        padding:6px 12px;
        margin:4px;
        background:#f0f0f0;
        border-radius:12px;
        font-size:14px;
        font-weight:500;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<div class="title"> SkillSync</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Match your resume with job descriptions instantly</div>', unsafe_allow_html=True)


col1, col2 = st.columns([1, 1])

with col1:
    resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

with col2:
    job_description = st.text_area("💼 Paste Job Description")

if st.button("🚀 Start Analysis"):
    if resume_file and job_description:
        resume_text = extract_text_from_pdf(resume_file)
        resume_keywords = get_top_keywords(resume_text, 20)
        jd_keywords = get_top_keywords(job_description, 20)
        score = match_score(resume_keywords, jd_keywords)

        st.markdown("---")
        st.subheader("📊 Match Results")

        st.progress(score / 100)
        st.metric("Match Score", f"{score}%")

        k1, k2 = st.columns(2)
        with k1:
            st.write("✅ **Resume Keywords**")
            st.markdown(" ".join([f"<span class='keyword-box'>{kw}</span>" for kw in resume_keywords]), unsafe_allow_html=True)
        with k2:
            st.write("💼 **JD Keywords**")
            st.markdown(" ".join([f"<span class='keyword-box'>{kw}</span>" for kw in jd_keywords]), unsafe_allow_html=True)

        missing = [w for w in jd_keywords if w not in resume_keywords]
        if missing:
            st.warning("⚠️ Missing important keywords: " + ", ".join(missing))
        else:
            st.success("🎉 Great! Your resume covers all major keywords.")

        with st.expander("📃 View Extracted Resume Text"):
            st.text(resume_text)
    else:
        st.error("⚠️ Please upload a resume and paste a job description before analyzing.")

# Footer
st.markdown("---")
st.caption("🚀 Built with Python & Streamlit | Project: SkillSync")
