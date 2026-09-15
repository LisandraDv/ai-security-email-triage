# 🛡️ LSDR Security AI Triage

### AI-assisted email security analysis for everyday users

**LSDR Security AI Triage** is a personal cybersecurity and AI project designed to help people who may not have a technical or cybersecurity background better understand suspicious emails before interacting with them.

The tool uses a **local AI model** to analyze an email, identify what type of message it may be, estimate its priority, explain why it could be suspicious, recommend a safer next step, and help the user determine whether the email should be reported to an **IT or Cybersecurity team**.

> Built by **Lisandra Duvernay** as part of my Cloud Security & Cybersecurity portfolio.

---

## 🎯 Purpose

Cybersecurity attacks often begin with something as simple as an email.

Phishing, credential theft, fake password reset requests, malicious links, impersonation, and social engineering can be difficult to identify — especially for users who do not work in cybersecurity.

I built this project to provide a simple first layer of guidance.

Instead of expecting a user to immediately understand whether an email is malicious, the tool helps answer questions such as:

- What type of email could this be?
- Does it show signs of phishing or suspicious activity?
- How urgent could the situation be?
- Why might the email be considered suspicious?
- What should I do next?
- Should I report it to IT or Cybersecurity?

The goal is **not to replace security professionals**, but to help users make safer decisions and escalate suspicious activity when necessary.

---

## 👥 Who is this for?

This project can be useful for:

- Non-technical users
- Employees who receive suspicious emails
- Students learning cybersecurity awareness
- Small organizations without a dedicated SOC
- Help desk and IT support teams
- People learning how phishing and social engineering work

---

## ⚙️ How it works

```text
Suspicious Email
      ↓
Local AI Security Analysis
      ↓
Email Category
      ↓
Priority Assessment
      ↓
Explanation of Suspicious Indicators
      ↓
Recommended Action
      ↓
Suggested Response
      ↓
Report to IT / Cybersecurity if necessary
```

The AI does not automatically take action against the email.

The user remains in control of the final decision.

---

## 🧠 What the AI analyzes

The tool currently classifies emails into the following categories:

- **Security Incident**
- **Access Request**
- **Phishing Report**
- **General Support**
- **Other**

It also assigns one of four priority levels:

| Priority | Meaning |
|---|---|
| 🟢 Low | Routine or low-risk request |
| 🟡 Medium | Suspicious activity that should be reviewed |
| 🟠 High | Likely security threat, phishing, malware, or credential risk |
| 🔴 Critical | Clear or active high-impact security incident |

---

## ✨ Features

- 🤖 Local AI-powered email analysis
- 🎣 Phishing identification
- 🚨 Security priority classification
- 🧠 Human-readable explanation of why an email may be suspicious
- 🛡️ Recommended security actions
- ✉️ Suggested response generation
- 📊 CSV logging
- 📦 Structured JSON output
- 🔒 Local AI processing with Ollama
- 👤 Human review remains part of the decision process

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-black)
![Cybersecurity](https://img.shields.io/badge/Focus-Cybersecurity-purple)

**Technologies used:**

- Python
- Streamlit
- Ollama
- Llama 3.2
- JSON
- CSV
- Local LLM inference

---

## 🖥️ Application Interface

The application provides a simple interface where the user can enter:

```text
Sender
Subject
Email Body
```

After selecting **Analyze email**, the AI returns:

```text
Category

Priority

Summary

Why the email may be suspicious

Recommended Action

Suggested Response
```

The interface was intentionally designed to be understandable even for users without cybersecurity experience.

---

## 📧 Example

### Input

```text
From: user@example.com
Subject: Suspicious Microsoft 365 login

I received an email asking me to verify my Microsoft 365 password
using a link. The sender address looks unusual and I have not
entered my credentials.
```

### AI Analysis

```json
{
  "category": "Phishing Report",
  "priority": "High",
  "summary": "A suspicious email is requesting Microsoft 365 credential verification.",
  "reason": "The message contains indicators commonly associated with credential phishing.",
  "recommended_action": "Do not interact with the link. Report the message to the IT or Cybersecurity team for further investigation.",
  "suggested_response": "Thank you for reporting this message. Please do not click the link or enter your credentials while the security team reviews it."
}
```

---

## 🔐 Privacy-first approach

One of the main design decisions behind this project is the use of a **local AI model**.

The application uses **Ollama**, allowing the language model to run locally instead of requiring emails to be sent to an external AI API.

For this portfolio demonstration:

- Use synthetic or non-sensitive emails.
- Do not upload confidential company information.
- Do not include real passwords or authentication tokens.
- Do not include tenant IDs or internal infrastructure details.
- Do not use confidential incident information.

The project is intended as a demonstration of AI-assisted cybersecurity awareness and triage.

---

## ⚠️ Important

This tool is an **AI-assisted security awareness and decision-support project**.

It is not intended to replace:

- Security analysts
- SOC teams
- Incident response procedures
- Email security gateways
- Microsoft Defender
- SIEM/SOAR platforms
- Organizational security policies

AI responses can be incorrect.

When an email appears suspicious, users should follow their organization's security procedures and report the message to the appropriate **IT or Cybersecurity team**.

---

# 🚀 Run the project locally

## 1. Install Python

Use Python 3.10 or newer.

Check your version:

```bash
python --version
```

---

## 2. Install Ollama

Install Ollama on your computer.

Then download the local model used by the project:

```bash
ollama pull llama3.2:3b
```

Verify the model:

```bash
ollama run llama3.2:3b
```

---

## 3. Create a virtual environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run the application

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## 🤖 Automation mode

The repository also includes an automation example.

The workflow can process `.txt` email files placed inside an `inbox` directory.

Run:

```bash
python automation.py
```

The workflow performs:

```text
Email File
    ↓
AI Analysis
    ↓
Security Classification
    ↓
Priority
    ↓
Recommended Action
    ↓
JSON Result
    ↓
CSV Log
```

This demonstrates how the project could later evolve from a manual analysis tool into an automated security workflow.

---

## 🔭 Future Improvements

Some features I would like to explore next include:

- IOC extraction from emails
- URL and domain reputation analysis
- Detection of IP addresses, domains and hashes
- Microsoft Graph integration
- Gmail integration
- Microsoft Teams security notifications
- Security dashboard and analytics
- MITRE ATT&CK mapping
- QR code phishing detection
- Attachment analysis
- Human approval workflows
- Improved social engineering detection
- Explainable phishing indicators
- Security awareness recommendations

---

## 💡 Project Vision

My goal with this project is to explore how **Artificial Intelligence can make cybersecurity knowledge more accessible to everyday users**.

Security tools are often designed for security professionals.

This project explores a different question:

> **Can AI help a person who does not understand cybersecurity recognize when something may be wrong before they click?**

LSDR Security AI Triage is my experiment toward answering that question.

---

## 👩‍💻 About the Author

**Lisandra Duvernay**

Cloud Security • Cybersecurity • IAM • Microsoft Security • Infrastructure

I am interested in building projects around:

- Cloud Security
- Identity & Access Management
- Microsoft Security
- Security Automation
- AI for Cybersecurity
- Infrastructure Security
- SecOps

### GitHub

https://github.com/LisandraDv

---

## 📌 Portfolio Project

This project is part of my personal cybersecurity portfolio and was created to demonstrate the practical combination of:

**Artificial Intelligence + Cybersecurity + Automation + Security Awareness**

---

### Built with 🛡️ by Lisandra Duvernay
