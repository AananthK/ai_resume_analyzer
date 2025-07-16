import streamlit as st

print("streamlit has been imported") # logging

from resume_utils import extract_text_from_pdf, extract_keywords, compare_keywords

print("resume_utils functions have been imported") # logging

import time

st.set_page_config(page_title="ATS Resume Analyzer")
st.title("📄 Resume vs Job Description Analyzer")

st.markdown("Upload your resume and paste the job description to analyze the keyword match.")

resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("📋 Paste Job Description")

if resume_file and jd_text:
    with st.spinner("Analyzing..."):
        time.sleep(2)
        resume_text = extract_text_from_pdf(resume_file)
        resume_keywords = extract_keywords(resume_text)
        jd_keywords = extract_keywords(jd_text)
        matched, missing, score = compare_keywords(resume_keywords, jd_keywords)

    st.subheader("✅ Match Score")
    st.progress(score)
    st.success(f"Your resume matches **{score}%** of the job description.")

    st.subheader("✔️ Matched Keywords")
    st.write(sorted(matched))

    st.subheader("❌ Missing Keywords")
    st.write(sorted(missing))

else:
    st.info("Upload a resume and paste a job description to get started.")