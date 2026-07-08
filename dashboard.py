import streamlit as st

def show_dashboard(results):

    if len(results) == 0:
        return

    total_candidates = len(results)

    highest_score = max(candidate["score"] for candidate in results)

    average_score = sum(candidate["score"] for candidate in results) / total_candidates

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "👥 Total Candidates",
            total_candidates
        )

    with col2:
        st.metric(
            "🏆 Highest Score",
            f"{highest_score}%"
        )

    with col3:
        st.metric(
            "📈 Average Score",
            f"{average_score:.1f}%"
        )

    st.divider()