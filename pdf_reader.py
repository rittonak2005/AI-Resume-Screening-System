import fitz  # PyMuPDF
import streamlit as st


def extract_text_from_pdf(uploaded_file):

    try:

        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        text = ""

        for page in pdf:
            text += page.get_text()

        if text.strip() == "":
            st.warning("⚠️ No text found in the uploaded PDF.")
            return ""

        return text

    except Exception as e:

        st.error(f"❌ Error reading PDF: {e}")
        return ""