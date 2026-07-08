import streamlit as st
from datetime import datetime


def show_header():

    st.markdown(
        """
        <h1 style='text-align:center;color:#1f77b4;'>
        📄 AI Resume Screening System
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h4 style='text-align:center;color:gray;'>
        AI Powered Resume Screening using Google Gemini
        </h4>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"📅 Date : {datetime.now().strftime('%d-%m-%Y')}")

    with col2:
        st.info("👨‍💻 Developer : Rittona")

    st.divider()