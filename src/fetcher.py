import requests


def fetch_trending(language="", since="daily", count=10):
    url = "https://api.gitterapp.com/repositories"
    params = {}
    if language:
        params["language"] = language
    if since:
        params["since"] = since

    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    repos = resp.json()

    results = []
    for repo in repos[:count]:
        results.append({
            "name": repo.get("fullName", repo.get("full_name", "")),
            "description": repo.get("description", ""),
            "url": repo.get("url", ""),
            "stars": repo.get("stars", repo.get("stargazers_count", 0)),
            "language": repo.get("language", ""),
            "forks": repo.get("forks", repo.get("forks_count", 0)),
            "author": repo.get("author", repo.get("owner", "")),
        })

    return results
