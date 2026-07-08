import streamlit as st


def apply_custom_style():

    st.markdown(
        """
        <style>

        .main {
            background-color: #f5f7fa;
        }

        .stButton>button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            height: 3em;
            font-size: 18px;
            font-weight: bold;
        }

        .stDownloadButton>button {
            width: 100%;
            background-color: #2196F3;
            color: white;
            border-radius: 10px;
            height: 3em;
            font-size: 16px;
            font-weight: bold;
        }

        div[data-testid="metric-container"] {
            background-color: white;
            border: 1px solid #dddddd;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        }

        </style>
        """,
        unsafe_allow_html=True
    )


def sidebar():

    st.sidebar.title("📄 AI Resume Screening")

    st.sidebar.info(
        """
Welcome!

Upload one or more resumes.

Paste a Job Description.

Click **Analyze Resumes**.

Ask questions using the AI HR Chatbot.

Download the Excel report after analysis.
        """
    )

    st.sidebar.success("Developed using Streamlit + Gemini AI")