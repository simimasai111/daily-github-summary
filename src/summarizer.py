import requests


def summarize_repos(repos, base_url, api_key, model, language="中文"):
    url = f"{base_url}/v1/chat/completions"

    repos_text = "\n\n".join([
        f"{i+1}. {r['name']}\n"
        f"   描述: {r.get('description', '暂无')}\n"
        f"   语言: {r.get('language', 'N/A')} | Stars: {r['stars']:,}"
        for i, r in enumerate(repos)
    ])

    prompt = f"""你是一个 GitHub 项目分析师。以下是今日 GitHub Trending 上的热门项目列表。

请为每个项目撰写一段详细的中文介绍（2-3句话），涵盖：
1. 核心功能：这个项目是做什么的？
2. 技术亮点：用了什么技术栈？有什么特别之处？
3. 适用场景：谁适合用？用来解决什么问题？

要求：
- 语言：{language}
- 每段介绍要充实具体，不要套话
- 无需重复项目名，直接写介绍内容
- 按序号逐行输出，格式为「1. 介绍内容」每个项目占一段

--- 项目列表 ---
{repos_text}"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是一个专业的 GitHub 项目分析师，擅长用生动的中文介绍开源项目。"},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 3000,
    }

    resp = requests.post(url, headers=headers, json=body, timeout=120)
    resp.raise_for_status()
    result = resp.json()

    return result["choices"][0]["message"]["content"]
