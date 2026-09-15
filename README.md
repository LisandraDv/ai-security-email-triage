# 🛡️ AI-Powered Security Email Triage

A personal project that uses a **local AI model** to classify security-related emails, assign a priority, recommend a next action, and draft a suggested response.

The project is intentionally designed to run from a **personal GitHub repository** without using a company Microsoft 365 tenant, corporate mailbox, or employer credentials.

## Why I built it

Security and IT teams receive many different types of emails: phishing reports, access requests, suspicious activity, routine support, and incident notifications.

Manually reviewing each message can slow down response times. This project demonstrates how AI can support first-level triage while keeping the final decision with a human analyst.

## Workflow

```text
Incoming Email
      ↓
Local AI Model
      ↓
Category Classification
      ↓
Priority Assignment
      ↓
Recommended Action
      ↓
Suggested Response
      ↓
CSV Log / JSON Output
```

## Categories

- Security Incident
- Access Request
- Phishing Report
- General Support
- Other

## Priority levels

- Low
- Medium
- High
- Critical

## Features

- Local AI inference using Ollama
- Streamlit web interface
- Automated folder-based processing
- Structured JSON output
- CSV triage logging
- Synthetic sample emails
- No company account or corporate API credentials required

## Tech stack

- Python
- Streamlit
- Ollama
- Local LLM
- JSON / CSV

## Quick start

### 1. Install Python

Use Python 3.10+.

### 2. Install Ollama

Install Ollama on your computer, then pull a lightweight model:

```bash
ollama pull llama3.2:3b
```

Start Ollama if it is not already running:

```bash
ollama serve
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the web app

```bash
streamlit run app.py
```

### 6. Run the automation demo

Put one or more `.txt` email files inside the `inbox` folder, then run:

```bash
python automation.py
```

The structured results will be written to the `processed` folder.

## Example input

```text
From: user@example.com
Subject: Suspicious Microsoft login page

I received an email asking me to verify my Microsoft 365 password.
The link opens a page that looks unusual and I have not entered my credentials.
```

Example AI result:

```json
{
  "category": "Phishing Report",
  "priority": "High",
  "summary": "User reported a suspicious credential-harvesting email.",
  "reason": "The message contains a suspicious login link requesting credentials.",
  "suggested_response": "Thank you for reporting this message. Please do not click the link or enter your credentials while the security team reviews it.",
  "recommended_action": "Quarantine the message and inspect the sender, URL, and related indicators."
}
```

## Security and privacy

This repository is a portfolio demonstration.

- Use only synthetic or non-sensitive data.
- Do not upload company emails, tenant IDs, internal domains, credentials, or confidential incident details.
- AI output should assist an analyst, not replace security judgment.

## Possible next improvements

- Microsoft Graph integration using a personal developer tenant
- Gmail API integration
- Microsoft Teams / Slack notifications
- IOC extraction
- URL reputation checks
- MITRE ATT&CK mapping
- Dashboard analytics
- Human approval before sending a response

## Application description

> I built an AI-powered security email triage workflow that uses a local language model to classify incoming messages by security category and priority, recommend the next action, and draft a response. The project demonstrates how AI can reduce manual triage effort while keeping sensitive data local and preserving human review.

## Author

Built as a personal cloud security and cybersecurity portfolio project.
