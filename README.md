# 每日 GitHub 项目汇总

通过 GitHub Actions 定时抓取 GitHub Trending，AI 总结后推送到手机。

## 使用方式

### 1. Fork 本仓库

### 2. 配置 GitHub Secrets

在仓库 Settings > Secrets and variables > Actions 中添加：

| Secret | 说明 |
|--------|------|
| `AI_BASE_URL` | AI API 地址，如 `https://api.deepseek.com` |
| `AI_API_KEY` | API 密钥 |
| `AI_MODEL` | 模型 ID，如 `deepseek-chat` / `gpt-4o-mini` |
| `SERVERCHAN_SENDKEY` | Server 酱 SendKey |

### 3. 启用 Actions

Actions 默认会在每天 UTC 01:00（北京时间 09:00）自动执行。也可在 Actions 页面手动触发 `workflow_dispatch`。

## 本地测试

```bash
pip install -r requirements.txt

AI_BASE_URL=... \
AI_API_KEY=... \
AI_MODEL=... \
SERVERCHAN_SENDKEY=... \
python src/main.py
```

## 技术栈

- Python + requests
- GitHub Actions
- OpenAI 兼容 API
- Server 酱 推送
