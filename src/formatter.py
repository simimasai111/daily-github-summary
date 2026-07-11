import re
from datetime import date


def _parse_summaries(text):
    summaries = {}
    lines = text.strip().split("\n")
    current_idx = None
    current_lines = []

    for line in lines:
        match = re.match(r"^(\d+)[.、]\s*(.*)", line)
        if match:
            if current_idx is not None:
                summaries[current_idx] = "\n".join(current_lines).strip()
            current_idx = int(match.group(1))
            current_lines = [match.group(2)]
        elif current_idx is not None:
            current_lines.append(line)

    if current_idx is not None:
        summaries[current_idx] = "\n".join(current_lines).strip()

    return summaries


def format_markdown(repos, summary_text):
    today = date.today().strftime("%Y-%m-%d")
    summaries = _parse_summaries(summary_text)

    lines = []
    lines.append(f"# 每日 GitHub 项目汇总 — {today}")
    lines.append("")
    lines.append(f"共 **{len(repos)}** 个项目 | 数据来源: GitHub Trending")
    lines.append("")
    lines.append("---")
    lines.append("")

    for i, repo in enumerate(repos, 1):
        lines.append(f"## [{repo['name']}]({repo['url']})")

        info = [f"⭐ **{repo['stars']:,}**"]
        if repo.get("language"):
            info.append(f"🔤 {repo['language']}")
        if repo.get("forks"):
            info.append(f"🍴 {repo['forks']:,}")

        lines.append(" | ".join(info))
        lines.append("")

        ai_summary = summaries.get(i, "")
        if ai_summary:
            lines.append(ai_summary)
            lines.append("")

        if repo.get("description"):
            lines.append(f"> {repo['description']}")
            lines.append("")

        lines.append("---")
        lines.append("")

    lines.append("*Powered by GitHub Actions & AI*")

    return "\n".join(lines)
