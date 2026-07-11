import requests


def push(title, markdown_content, sendkey):
    url = f"https://sctapi.ftqq.com/{sendkey}.send"
    body = {
        "title": title,
        "md": markdown_content,
    }
    resp = requests.post(url, json=body, timeout=30)
    resp.raise_for_status()
    return resp.json()
