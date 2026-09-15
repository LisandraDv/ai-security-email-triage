"""
Simple automation demo:
- Reads .txt files from ./inbox
- Sends each one to the local AI triage engine
- Writes the result to ./processed as JSON
- Logs the result to ./data/triage_log.csv

This intentionally avoids Microsoft 365/Gmail credentials so the repository
can be demonstrated safely from a personal GitHub account.
"""

import json
from pathlib import Path

from ai_triage import triage_email, log_result

INBOX = Path("inbox")
PROCESSED = Path("processed")

INBOX.mkdir(exist_ok=True)
PROCESSED.mkdir(exist_ok=True)

def parse_email_file(text: str):
    sender = ""
    subject = ""
    body_lines = []

    for line in text.splitlines():
        if line.lower().startswith("from:") and not sender:
            sender = line.split(":", 1)[1].strip()
        elif line.lower().startswith("subject:") and not subject:
            subject = line.split(":", 1)[1].strip()
        else:
            body_lines.append(line)

    return sender, subject, "\n".join(body_lines).strip()

def main():
    files = sorted(INBOX.glob("*.txt"))
    if not files:
        print("No .txt files found in ./inbox")
        return

    for path in files:
        text = path.read_text(encoding="utf-8")
        sender, subject, body = parse_email_file(text)

        result = triage_email(subject, sender, body)
        log_result(subject, sender, result)

        output = {
            "source_file": path.name,
            "sender": sender,
            "subject": subject,
            **result,
        }

        out_path = PROCESSED / f"{path.stem}.json"
        out_path.write_text(
            json.dumps(output, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        print(f"Processed: {path.name} -> {out_path.name}")

if __name__ == "__main__":
    main()
