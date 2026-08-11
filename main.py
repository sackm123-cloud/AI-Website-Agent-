import argparse
import logging
import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

LOGGER = logging.getLogger("ai-automation")

IST = ZoneInfo("Asia/Kolkata")


def now_ist():
    return datetime.now(IST)


def run_news():
    from news_agent import run
    return run()


def run_class():
    from class_agent import run
    return run()


def run_stem_tip():
    from stem_tip_agent import run
    return run()


def run_project():
    from project_agent import run
    return run()


def run_weekly():
    from weekly_report_agent import run
    return run()


def run_competition():
    from competition_agent import run
    return run()


AGENTS = {
    "news": run_news,
    "class": run_class,
    "stem_tip": run_stem_tip,
    "project": run_project,
    "weekly": run_weekly,
    "competition": run_competition,
}


def run_agent(name):
    if name not in AGENTS:
        raise ValueError(f"Unknown agent: {name}")

    LOGGER.info("Starting agent: %s", name)

    try:
        result = AGENTS[name]()

        LOGGER.info("Agent completed: %s", name)

        if result:
            LOGGER.info("Result: %s", str(result)[:500])

        return result

    except Exception:
        LOGGER.exception("Agent failed: %s", name)
        raise


def run_all():
    results = {}

    for name in AGENTS:
        try:
            results[name] = run_agent(name)
        except Exception as exc:
            results[name] = {
                "status": "failed",
                "error": str(exc),
            }

    return results


def main():
    parser = argparse.ArgumentParser(
        description="AI STEM Automation Agent"
    )

    parser.add_argument(
        "--agent",
        default="all",
        choices=["all"] + list(AGENTS.keys()),
        help="Agent to execute",
    )

    args = parser.parse_args()

    LOGGER.info(
        "AI Automation started | %s",
        now_ist().strftime("%Y-%m-%d %H:%M:%S IST"),
    )

    if args.agent == "all":
        results = run_all()
        LOGGER.info("All agents completed")
        return 0 if results else 1

    run_agent(args.agent)
    return 0


if __name__ == "__main__":
    sys.exit(main())
