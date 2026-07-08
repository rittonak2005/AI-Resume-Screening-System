import streamlit as st

def show_best_candidate(results):

    if len(results) == 0:
        return

    best = results[0]

    st.success("🏆 Best Candidate")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Candidate",
            best["name"]
        )

    with col2:
        st.metric(
            "Match Score",
            f"{best['score']}%"
        )

    with col3:
        st.metric(
            "Recommendation",
            best["recommendation"]
        )

    st.divider()