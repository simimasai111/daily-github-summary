import sys
from config import get_config
from fetcher import fetch_trending
from summarizer import summarize_repos
from formatter import format_markdown
from pusher import push


def main():
    config = get_config()

    print("获取 GitHub Trending 项目...")
    repos = fetch_trending(count=config["repo_count"])
    print(f"获取到 {len(repos)} 个项目")

    print("调用 AI 进行总结...")
    summary = summarize_repos(
        repos,
        config["ai_base_url"],
        config["ai_api_key"],
        config["ai_model"],
        config["summary_language"],
    )
    print("AI 总结完成")

    print("格式化 Markdown...")
    markdown = format_markdown(repos, summary)

    print("推送到 Server 酱...")
    result = push(
        f"每日 GitHub 项目汇总 ({len(repos)} 个项目)",
        markdown,
        config["serverchan_sendkey"],
    )

    if result.get("code") == 0:
        print("推送成功！")
    else:
        print(f"推送失败: {result}")
        sys.exit(1)


if __name__ == "__main__":
    main()
