import streamlit as st
from pdf_reader import extract_text_from_pdf
from resume_analyzer import analyze_resume
from session_manager import (
    initialize_session,
    save_results,
    get_results
)
from display import display_results
from style import apply_custom_style, sidebar
from header import show_header

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# ----------------------------------
# Initialize Session
# ----------------------------------
initialize_session()

# ----------------------------------
# Apply Custom Style
# ----------------------------------
apply_custom_style()
sidebar()

# ----------------------------------
# Header
# ----------------------------------
show_header()

# ----------------------------------
# Resume Upload
# ----------------------------------
st.subheader("📂 Upload Resume PDFs")

uploaded_resumes = st.file_uploader(
    "Choose one or more PDF resumes",
    type=["pdf"],
    accept_multiple_files=True
)

st.divider()

# ----------------------------------
# Job Description
# ----------------------------------
st.subheader("📝 Job Description")

job_description = st.text_area(
    "Paste the Job Description here",
    height=250,
    placeholder="""Example:

Job Title: Data Analyst

Skills Required:
- Python
- SQL
- Power BI
- Excel
"""
)

st.divider()

# ----------------------------------
# Analyze Button
# ----------------------------------
if uploaded_resumes and job_description:

    if st.button("🚀 Analyze Resumes"):

        results = []
        all_analysis = []

        for resume in uploaded_resumes:

            resume_text = extract_text_from_pdf(resume)

            with st.spinner(f"Analyzing {resume.name}..."):

                analysis = analyze_resume(
                    resume_text,
                    job_description
                )

            all_analysis.append({
                "name": resume.name,
                "analysis": analysis
            })

            results.append({
                "name": resume.name,
                "score": analysis["match_score"],
                "recommendation": analysis["recommendation"]
            })

        # Sort Candidates
        results = sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )

        # Save Results
        save_results(results, all_analysis)

# ----------------------------------
# Display Results
# ----------------------------------
results, all_analysis = get_results()

if results:
    display_results(results, all_analysis)