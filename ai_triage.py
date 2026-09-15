import json
import os
from datetime import datetime
from pathlib import Path

import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

ALLOWED_CATEGORIES = {
    "Security Incident",
    "Access Request",
    "Phishing Report",
    "General Support",
    "Other",
}

ALLOWED_PRIORITIES = {"Low", "Medium", "High", "Critical"}

SYSTEM_PROMPT = """
You are a cybersecurity triage assistant.

Analyze the email and return STRICT JSON only, with this schema:
{
  "category": "Security Incident | Access Request | Phishing Report | General Support | Other",
  "priority": "Low | Medium | High | Critical",
  "summary": "one short sentence",
  "reason": "one short sentence explaining why the category and priority were selected",
  "suggested_response": "a short, professional email response",
  "recommended_action": "one short next-step recommendation"
}

Rules:
- Use Critical only for clear urgent/high-impact security situations.
- Use High for likely compromise, active phishing, malware, credential theft, or major access risk.
- Use Medium for suspicious but not confirmed security issues, or access requests requiring review.
- Use Low for routine support or informational requests.
- Never invent facts that are not present in the email.
- Keep the suggested response concise and professional.
"""

def _clean_result(result: dict) -> dict:
    category = result.get("category", "Other")
    priority = result.get("priority", "Low")

    if category not in ALLOWED_CATEGORIES:
        category = "Other"
    if priority not in ALLOWED_PRIORITIES:
        priority = "Low"

    return {
        "category": category,
        "priority": priority,
        "summary": str(result.get("summary", "")).strip(),
        "reason": str(result.get("reason", "")).strip(),
        "suggested_response": str(result.get("suggested_response", "")).strip(),
        "recommended_action": str(result.get("recommended_action", "")).strip(),
    }

def triage_email(subject: str, sender: str, body: str) -> dict:
    prompt = f"""
{SYSTEM_PROMPT}

EMAIL
From: {sender or "Unknown"}
Subject: {subject or "(No subject)"}

Body:
{body}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "format": "json",
        },
        timeout=120,
    )
    response.raise_for_status()

    payload = response.json()
    raw = payload.get("response", "{}")
    result = json.loads(raw)
    return _clean_result(result)

def log_result(subject: str, sender: str, result: dict, path: str = "data/triage_log.csv") -> None:
    import csv

    log_path = Path(path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    exists = log_path.exists()

    with log_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow([
                "timestamp",
                "sender",
                "subject",
                "category",
                "priority",
                "summary",
                "recommended_action",
            ])
        writer.writerow([
            datetime.utcnow().isoformat() + "Z",
            sender,
            subject,
            result.get("category", ""),
            result.get("priority", ""),
            result.get("summary", ""),
            result.get("recommended_action", ""),
        ])
