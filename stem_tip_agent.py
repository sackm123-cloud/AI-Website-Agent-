from datetime import datetime
from zoneinfo import ZoneInfo

from gemini import generate
from gmail import send_email


def run():
    date = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%d %B %Y")

    prompt = f"""
Create today's STEM experiment for a school STEM educator.

Date: {date}

Focus on one practical experiment involving:

- Arduino
- ESP32
- electronics
- robotics
- sensors
- IoT
- AI
- 3D printing

Include:

💡 STEM TIP OF THE DAY

Experiment:
Learning objective:
Components:
Circuit concept:
Procedure:
Expected result:
Safety:
Extension challenge:

Keep it suitable for school students.
Make the experiment realistically buildable.
"""

    content = generate(prompt)

    send_email(
        subject=f"💡 Daily STEM Tip — {date}",
        body=content,
    )

    return content
