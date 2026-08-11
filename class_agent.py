from datetime import datetime
from zoneinfo import ZoneInfo

from gemini import generate
from gmail import send_email


def run(session_data=None):
    date = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%d %B %Y")

    if not session_data:
        session_data = """
No class data was entered today.
Generate a template requesting today's
grade-wise STEM session information.
"""

    prompt = f"""
You are a STEM education reporting assistant.

Date: {date}

Create a concise grade-wise STEM class report.

Session data:

{session_data}

Format:

📚 STEM CLASS UPDATE

Grade X:
Topic:
Activity:
Learning outcome:

Grade X:
Topic:
Activity:
Learning outcome:

Then include:

🎯 Overall Learning Outcome

📝 Teacher Note

Keep each grade to 2-3 lines.
"""

    content = generate(prompt)

    send_email(
        subject=f"📚 STEM Class Update — {date}",
        body=content,
    )

    return content
