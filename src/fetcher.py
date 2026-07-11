import re
import requests
from bs4 import BeautifulSoup


def _parse_stars(text):
    cleaned = re.sub(r"[^0-9]", "", text)
    return int(cleaned) if cleaned else 0


def fetch_trending(language="", since="daily", count=10):
    url = f"https://github.com/trending/{language}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    params = {"since": since}

    resp = requests.get(url, params=params, headers=headers, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    articles = soup.select("article.Box-row")[:count]

    results = []
    for article in articles:
        h2 = article.find("h2")
        a_tag = h2.find("a") if h2 else None
        full_href = a_tag["href"].strip("/") if a_tag and a_tag.get("href") else ""
        name = full_href.replace("/", "/") if full_href else ""

        desc_p = article.find("p", class_=re.compile(r"color-fg-muted"))
        description = desc_p.get_text(strip=True) if desc_p else ""

        lang_span = article.find("span", itemprop="programmingLanguage")
        language = lang_span.get_text(strip=True) if lang_span else ""

        stars = 0
        forks = 0
        for link in article.find_all("a", href=re.compile(r"/stargazers$|/forks$")):
            href = link.get("href", "")
            num = _parse_stars(link.get_text())
            if "/stargazers" in href:
                stars = num
            elif "/forks" in href:
                forks = num

        parts = name.split("/", 1)
        author = parts[0] if len(parts) > 0 else ""
        clean_name = name

        results.append({
            "name": clean_name,
            "description": description,
            "url": f"https://github.com/{name}",
            "stars": stars,
            "language": language,
            "forks": forks,
            "author": author,
        })

    return results
