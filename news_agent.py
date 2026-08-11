from datetime import datetime
from zoneinfo import ZoneInfo

from gemini import generate
from gmail import send_email
from web_search import search_news


def run():
    today = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%d %B %Y")

    articles = search_news(
        "latest artificial intelligence robotics "
        "robotics education STEM electronics"
    )

    if not articles:
        raise RuntimeError(
            "No news articles were found"
        )

    source_text = "\n\n".join(
        f"TITLE: {item['title']}\n"
        f"URL: {item['url']}\n"
        f"SUMMARY: {item.get('summary', '')}"
        for item in articles[:10]
    )

    prompt = f"""
Create a concise daily AI and Robotics news briefing
for a STEM educator.

Date: {today}

Use these articles:

{source_text}

Format:

🤖 DAILY AI & ROBOTICS NEWS

1. Headline
   2-3 sentence explanation

2. Headline
   2-3 sentence explanation

3. Headline
   2-3 sentence explanation

🎯 STEM CLASSROOM IMPACT
Explain how today's developments could be useful
for students, robotics projects or STEM education.

Keep it practical and easy to read.
Do not invent facts or links.
"""

    content = generate(prompt)

    send_email(
        subject=f"🤖 Daily AI & Robotics News — {today}",
        body=content,
    )

    return content
