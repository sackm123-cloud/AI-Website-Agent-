import os
from datetime import datetime
from zoneinfo import ZoneInfo

import requests

from gemini import generate
from gmail import send_email


def get_repo_info(repo):
    token = os.getenv("GITHUB_TOKEN")

    headers = {
        "Accept": "application/vnd.github+json"
    }

    if token:
        headers["Authorization"] = (
            f"Bearer {token}"
        )

    response = requests.get(
        f"https://api.github.com/repos/{repo}",
        headers=headers,
        timeout=20,
    )

    response.raise_for_status()

    return response.json()


def run():
    repo = os.getenv(
        "GITHUB_REPO",
        "sackm123-cloud/Kaggriculture-competition",
    )

    info = get_repo_info(repo)

    date = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%d %B %Y")

    prompt = f"""
Analyze this GitHub project progress.

Date:
{date}

Repository:
{repo}

Repository name:
{info.get("name")}

Description:
{info.get("description")}

Stars:
{info.get("stargazers_count")}

Forks:
{info.get("forks_count")}

Open issues:
{info.get("open_issues_count")}

Last update:
{info.get("updated_at")}

Create:

🏆 PROJECT / COMPETITION UPDATE

Current status:
Recent activity:
What is going well:
Potential problem:
Recommended next action:

Keep the report factual.
Do not claim a change occurred unless the data supports it.
"""

    content = generate(prompt)

    send_email(
        subject=f"🏆 Competition Update — {date}",
        body=content,
    )

    return content
