import requests


def summarize_repos(repos, base_url, api_key, model, language="中文"):
    url = f"{base_url}/v1/chat/completions"

    repos_text = "\n".join([
        f"{i+1}. [{r['name']}]({r['url']}) - ⭐ {r['stars']} | {r.get('language', 'N/A')}\n"
        f"   {r.get('description', '暂无描述')}"
        for i, r in enumerate(repos)
    ])

    prompt = f"""你是一个 GitHub 项目分析师。以下是今日 GitHub Trending 上的热门项目列表。

请用{language}为每个项目写一段简短的总结（50字以内），包括：
- 这个项目是做什么的
- 主要亮点或技术特点

要求：
1. 语言：{language}
2. 每个总结简洁有力，直击要点
3. 按序号输出，格式为「序号. 项目名 — 总结」

--- 项目列表 ---
{repos_text}"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是一个专业的 GitHub 项目分析师，擅长用简洁语言总结开源项目。"},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 2000,
    }

    resp = requests.post(url, headers=headers, json=body, timeout=60)
    resp.raise_for_status()
    result = resp.json()

    return result["choices"][0]["message"]["content"]
