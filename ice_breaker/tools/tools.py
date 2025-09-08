import re

from langchain_tavily import TavilySearch


def get_profile_url_tavily(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    search = TavilySearch()
    res = search.run(f"{name}")
    return res


HANDLE_RE = re.compile(
    r"(?:https?://)?(?:x\.com|twitter\.com)/([A-Za-z0-9_]{1,15})(?:/)?",
    re.IGNORECASE,
)


def get_twitter_profile_url(name: str) -> str:
    """
    Dedicated search for a person's Twitter/X profile page.
    Returns a URL like 'https://x.com/elonmusk' or 'NOT_FOUND'.
    """
    search = TavilySearch()
    query = f"{name} site:x.com OR site:twitter.com"
    # Pass query as positional argument
    results = search.run(query)

    # If results is a dict with "results", iterate as before
    for r in results.get("results", []):
        url = r.get("url", "")
        m = HANDLE_RE.search(url)
        if m:
            handle = m.group(1)
            return f"https://x.com/{handle}"

        snippet = r.get("content", "")
        m = HANDLE_RE.search(snippet)
        if m:
            handle = m.group(1)
            return f"https://x.com/{handle}"

    return "NOT_FOUND"
