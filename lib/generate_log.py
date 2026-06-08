from datetime import datetime
import requests

LOG_API_URL = "https://jsonplaceholder.typicode.com/posts/1"


def generate_log(data):
    """Write a list of log entries to a dated log file."""
    if not isinstance(data, list):
        raise ValueError("Log data must be provided as a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetch a sample post from the public JSONPlaceholder API."""
    response = requests.get(LOG_API_URL, timeout=10)
    response.raise_for_status()
    return response.json()


def build_log_entries():
    """Build a list of log entries including API fetch summary."""
    log_entries = [
        "Automation run started",
        "Fetching sample API data",
    ]

    try:
        post = fetch_data()
        log_entries.append(f"Fetched post title: {post.get('title', 'N/A')}")
        log_entries.append("API fetch completed successfully")
    except Exception as exc:
        log_entries.append(f"API fetch failed: {exc}")

    log_entries.append("Automation run finished")
    return log_entries


if __name__ == "__main__":
    entries = build_log_entries()
    generate_log(entries)
