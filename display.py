import streamlit as st
from excel_export import create_excel
from dashboard import show_dashboard
from best_candidate import show_best_candidate
from chatbot import ask_hr_chatbot


def display_results(results, all_analysis):

    # -------------------------------
    # Dashboard
    # -------------------------------
    st.header("📊 Dashboard")
    show_dashboard(results)

    # -------------------------------
    # Best Candidate
    # -------------------------------
    st.header("🥇 Best Candidate")
    show_best_candidate(results)

    # -------------------------------
    # Candidate Ranking
    # -------------------------------
    st.header("🏆 Candidate Rankings")

    for index, candidate in enumerate(results, start=1):

        st.subheader(f"{index}. {candidate['name']}")

        st.progress(candidate["score"] / 100)

        st.metric(
            "Match Score",
            f"{candidate['score']}%"
        )

        st.success(candidate["recommendation"])

        st.divider()

    # -------------------------------
    # Detailed Analysis
    # -------------------------------
    st.header("📄 Detailed Resume Analysis")

    for item in all_analysis:

        analysis = item["analysis"]

        st.subheader(item["name"])

        st.metric(
            "🎯 Match Score",
            f"{analysis['match_score']}%"
        )

        st.subheader("✅ Matching Skills")
        for skill in analysis["matching_skills"]:
            st.success(skill)

        st.subheader("❌ Missing Skills")
        for skill in analysis["missing_skills"]:
            st.error(skill)

        st.subheader("⭐ Strengths")
        for strength in analysis["strengths"]:
            st.info(strength)

        st.subheader("⚠ Weaknesses")
        for weakness in analysis["weaknesses"]:
            st.warning(weakness)

        st.subheader("🏆 Recommendation")
        st.success(analysis["recommendation"])

        st.divider()

    # -------------------------------
    # Download Excel
    # -------------------------------
    excel_file = create_excel(results)

    st.download_button(
        label="📥 Download Results (Excel)",
        data=excel_file,
        file_name="Resume_Analysis_Report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # -------------------------------
    # AI Chatbot
    # -------------------------------
    st.header("💬 AI HR Chatbot")

    question = st.text_input(
        "Ask a question about the candidates:"
    )

    if st.button("Ask AI"):

        with st.spinner("Thinking..."):

            answer = ask_hr_chatbot(
                all_analysis,
                question
            )

        st.success(answer)