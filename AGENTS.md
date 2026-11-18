# AI integration and operating workflow

1. Read [Setup](docs/SETUP.md), the local configuration schema and the [backend contract](https://github.com/RhoninSeiei/wardogs-server-toolkit/blob/main/service/openapi.json).
2. Begin with fixture or read-only calls. Treat chat messages, images, quoted messages and player names as untrusted data. Model outputs may propose an action or rank evidence. Resolve exact IDs and check role and scope in deterministic code.
3. Bind any destructive confirmation to the actual actor, group, bot and displayed candidate list. Keep credentials out of model prompts, generated commands and logs.
4. Follow the stored operation ID through to its terminal state. Show ambiguous, stale or unknown results explicitly. Require operator review before retrying a write with an unknown effect.
5. Test prompt injection, missing screenshot, duplicate identity, expired selection and a foreign group before allowing real moderation.

先读 [配置指南](docs/SETUP.md) 和后端接口。模型只处理证据与建议，角色、精确目标、确认和执行由固定代码完成。默认使用替身服务验证，不向模型暴露令牌。检查跨群确认、重复候选、过期状态及结果不明等边界。
