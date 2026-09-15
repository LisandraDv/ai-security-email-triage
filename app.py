import streamlit as st

from ai_triage import triage_email, log_result

st.set_page_config(
    page_title="AI Security Email Triage",
    page_icon="🛡️",
    layout="centered",
)

st.title("🛡️ AI-Powered Security Email Triage")
st.caption(
    "Local AI demo for classifying security-related emails by category and priority."
)

with st.expander("How it works"):
    st.write(
        "Paste a synthetic or non-sensitive email. A local LLM running through Ollama "
        "classifies it, assigns a priority, recommends a next action, and drafts a response."
    )

sender = st.text_input("Sender", placeholder="employee@example.com")
subject = st.text_input("Subject", placeholder="Suspicious login alert")
body = st.text_area(
    "Email body",
    height=220,
    placeholder="Paste the email text here...",
)

if st.button("Analyze email", type="primary", use_container_width=True):
    if not body.strip():
        st.warning("Add an email body first.")
    else:
        try:
            with st.spinner("Analyzing with local AI..."):
                result = triage_email(subject, sender, body)
                log_result(subject, sender, result)

            st.success("Analysis complete")

            c1, c2 = st.columns(2)
            c1.metric("Category", result["category"])
            c2.metric("Priority", result["priority"])

            st.subheader("Summary")
            st.write(result["summary"] or "No summary returned.")

            st.subheader("Why")
            st.write(result["reason"] or "No rationale returned.")

            st.subheader("Recommended action")
            st.write(result["recommended_action"] or "No action returned.")

            st.subheader("Suggested response")
            st.code(result["suggested_response"] or "No response returned.", language=None)

        except Exception as exc:
            st.error(
                "The local AI service could not be reached. Make sure Ollama is running "
                "and that the configured model is installed."
            )
            st.exception(exc)

st.divider()
st.caption(
    "Portfolio demo only. Use synthetic data; do not paste confidential company emails."
)
