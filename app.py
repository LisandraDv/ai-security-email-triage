import streamlit as st

from ai_triage import triage_email, log_result

st.set_page_config(
    page_title="LSDR Security AI Triage",
    page_icon="🛡️",
    layout="centered",
)

st.markdown(
    """
    <style>
        :root {
            --lsdr-accent: #a78bfa;
            --lsdr-accent-2: #67e8f9;
            --lsdr-panel: rgba(167, 139, 250, 0.08);
            --lsdr-border: rgba(167, 139, 250, 0.28);
        }

        .block-container {
            padding-top: 5rem !important;
            padding-bottom: 4rem;
        }

        .lsdr-brand {
            color: #EDE9FE !important;
            display: inline-flex;
            align-items: center;
            gap: .55rem;
            padding: .42rem .78rem;
            border: 1px solid var(--lsdr-border);
            border-radius: 999px;
            background: var(--lsdr-panel);
            font-size: .82rem;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }

        .lsdr-dot {
            width: .55rem;
            height: .55rem;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--lsdr-accent), var(--lsdr-accent-2));
            box-shadow: 0 0 16px rgba(103, 232, 249, .45);
        }

        .lsdr-title {
            font-size: clamp(2.2rem, 5vw, 3.5rem);
            line-height: 1.02;
            font-weight: 800;
            letter-spacing: -0.045em;
            margin: 0 0 .65rem 0;
        }

        .lsdr-gradient {
            background: linear-gradient(90deg, var(--lsdr-accent), var(--lsdr-accent-2));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .lsdr-subtitle {
            opacity: .78;
            font-size: 1rem;
            margin-bottom: 1.4rem;
        }

        .lsdr-stack {
            display: flex;
            flex-wrap: wrap;
            gap: .5rem;
            margin: .4rem 0 1.5rem 0;
        }

        .lsdr-chip {
            padding: .28rem .62rem;
            border-radius: 999px;
            border: 1px solid var(--lsdr-border);
            background: var(--lsdr-panel);
            font-size: .78rem;
            opacity: .9;
        }

        .lsdr-watermark {
            position: fixed;
            right: 2rem;
            bottom: 1.15rem;
            z-index: 0;
            font-size: clamp(4rem, 12vw, 9rem);
            font-weight: 900;
            letter-spacing: -.08em;
            opacity: 0.035;
            user-select: none;
            pointer-events: none;
        }

        .lsdr-footer {
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid var(--lsdr-border);
            text-align: center;
            font-size: .86rem;
            opacity: .78;
        }

        .lsdr-footer a {
            color: var(--lsdr-accent-2) !important;
            text-decoration: none;
            font-weight: 700;
        }

        div[data-testid="stMetric"] {
            border: 1px solid var(--lsdr-border);
            background: var(--lsdr-panel);
            padding: .85rem 1rem;
            border-radius: 16px;
        }

        div.stButton > button[kind="primary"] {
            border: 0;
            background: linear-gradient(90deg, #8b5cf6, #0891b2);
            font-weight: 700;
        }

        div.stButton > button[kind="primary"]:hover {
            border: 0;
            filter: brightness(1.08);
        }
    </style>

    <div class="lsdr-watermark">LSDR</div>

    <div class="lsdr-brand">
        <span class="lsdr-dot"></span>
        LSDR Security Lab
    </div>

    <div class="lsdr-title">
        🛡️ <span class="lsdr-gradient">LSDR Security AI Triage</span>
    </div>

    <div class="lsdr-subtitle">
        AI-assisted email triage for cybersecurity workflows — built as a personal cloud security portfolio project.
    </div>

    <div class="lsdr-stack">
        <span class="lsdr-chip">Python</span>
        <span class="lsdr-chip">Streamlit</span>
        <span class="lsdr-chip">Ollama</span>
        <span class="lsdr-chip">Local LLM</span>
        <span class="lsdr-chip">Cybersecurity</span>
    </div>
    """,
    unsafe_allow_html=True,
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

st.markdown(
    """
    <div class="lsdr-footer">
        <strong>Built by Lisandra Duvernay</strong> · Cloud Security & Cybersecurity Portfolio<br>
        <a href="https://github.com/LisandraDv" target="_blank">github.com/LisandraDv</a>
        &nbsp;·&nbsp; Local-first AI demo · Synthetic data only
    </div>
    """,
    unsafe_allow_html=True,
)
