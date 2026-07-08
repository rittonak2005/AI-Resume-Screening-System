import streamlit as st


def initialize_session():
    if "results" not in st.session_state:
        st.session_state.results = []

    if "all_analysis" not in st.session_state:
        st.session_state.all_analysis = []


def save_results(results, all_analysis):
    st.session_state.results = results
    st.session_state.all_analysis = all_analysis


def get_results():
    return (
        st.session_state.results,
        st.session_state.all_analysis
    )


def clear_results():
    st.session_state.results = []
    st.session_state.all_analysis = []