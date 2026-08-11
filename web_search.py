import html
import re

import requests
from bs4 import BeautifulSoup


GOOGLE_NEWS_RSS = (
    "https://news.google.com/rss/search"
    "?q={query}"
    "&hl=en-IN"
    "&gl=IN"
    "&ceid=IN:en"
)


def clean_text(text):
    text = html.unescape(text or "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def search_news(query, limit=10):
    url = GOOGLE_NEWS_RSS.format(
        query=requests.utils.quote(query)
    )

    response = requests.get(
        url,
        timeout=20,
        headers={
            "User-Agent": "AI-STEM-Automation/1.0"
        },
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.content,
        "xml",
    )

    results = []

    for item in soup.find_all("item")[:limit]:
        title = clean_text(
            item.title.text if item.title else ""
        )

        link = (
            item.link.text.strip()
            if item.link
            else ""
        )

        description = clean_text(
            item.description.text
            if item.description
            else ""
        )

        if title and link:
            results.append(
                {
                    "title": title,
                    "url": link,
                    "summary": description,
                }
            )

    return results
