from datetime import date


def format_markdown(repos, summary_text):
    today = date.today().strftime("%Y-%m-%d")

    lines = []
    lines.append(f"# 每日 GitHub 项目汇总 — {today}")
    lines.append("")
    lines.append("> 由 AI 自动生成，每日推送")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(summary_text)
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 完整数据")
    lines.append("")

    for r in repos:
        lines.append(f"### [{r['name']}]({r['url']})")
        lines.append(f"- Stars: **{r['stars']}**")
        lang = r.get("language", "N/A")
        if lang:
            lines.append(f"- 语言: {lang}")
        desc = r.get("description", "")
        if desc:
            lines.append(f"- 简介: {desc}")
        lines.append("")

    lines.append("*Powered by GitHub Actions & AI*")

    return "\n".join(lines)
