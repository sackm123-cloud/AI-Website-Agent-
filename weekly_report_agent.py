from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from gemini import generate
from gmail import send_email


def run(weekly_data=None):
    now = datetime.now(
        ZoneInfo("Asia/Kolkata")
    )

    week_start = now - timedelta(
        days=now.weekday()
    )

    if not weekly_data:
        weekly_data = """
No weekly activity data has been connected yet.
Generate a useful weekly report template.
"""

    prompt = f"""
Create a professional weekly STEM activity report.

Week beginning:
{week_start.strftime("%d %B %Y")}

Activities:

{weekly_data}

Include:

📊 WEEKLY STEM PROGRESS REPORT

1. Major activities
2. Classes conducted
3. Robotics/electronics activities
4. Student learning outcomes
5. Projects completed
6. Challenges/issues
7. Recommended next steps

Keep it concise and professional.
"""

    content = generate(prompt)

    send_email(
        subject="📊 Weekly STEM Progress Report",
        body=content,
    )

    return content
