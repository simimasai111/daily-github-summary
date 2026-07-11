import os


def get_config():
    return {
        "ai_base_url": os.environ.get("AI_BASE_URL", "https://api.openai.com").rstrip("/"),
        "ai_api_key": os.environ.get("AI_API_KEY", ""),
        "ai_model": os.environ.get("AI_MODEL", "gpt-4o-mini"),
        "serverchan_sendkey": os.environ.get("SERVERCHAN_SENDKEY", ""),
        "repo_count": int(os.environ.get("REPO_COUNT", "10")),
        "summary_language": os.environ.get("SUMMARY_LANGUAGE", "中文"),
    }
