# Setup and operation · 配置与使用

1. Put the bot and management backend on a trusted network. Set `service_base` to an address reachable from the AstrBot process. In containers, localhost usually points to AstrBot itself. Mount credentials as readable files instead of putting tokens in chat or in the plugin configuration.
2. Configure `service_token_file` for queries. For OneBot, set the adapter's exact `platform_id`, `bot_account_id` and `allowed_groups`. For QQ Official, configure `official_query_scopes` or `official_admin_scopes` from actual adapter identities. See `_conf_schema.json` for field types.
3. Enable `public_queries_enabled` for the approved scope, mention the bot and ask “服务器现在多少人” or “现在比分”. Validate that a second, unlisted scope is denied. Use `default_provider_id` for text and `assessment_provider_id` for vision. Empty IDs use AstrBot's active chat provider. Set an optional `fallback_provider_id` available on the same instance.
4. When needed, set `admin_execution_token_file` and `admin_kicks_enabled`, with matching backend scopes and verified group roles. Use a test group and substitute backend first. Mention the bot with “回溯”, “处罚记录 玩家昵称” or “封禁原因 SteamID64”; allow the plugin to resolve the candidate. If the workflow presents a numbered choice, use the number in the same group and bot conversation within its confirmation window.
5. Report auto-execution is opt-in. Supply `execution_token_file` and intentionally enable `auto_execute` only after testing representative evidence and ambiguous cases. Check image-provider privacy, media host allowlists, and local data retention. Keep automatic join approvals and server ID notices disabled unless explicitly needed.

令牌通过文件挂载，按用途隔离。分别确认机器人、群和管理员角色，并与管理后端范围匹配。先在测试群核验只读查询、错群拒绝和候选确认，再决定是否启用处罚写入。普通成员举报与管理指令权限分离。截图供应商可能收到玩家昵称或图片，请按社区规则控制数据范围。

## Troubleshooting · 排查

- Empty roster or stale data: check backend health, RCON reachability and cache freshness. Treat missing evidence as unavailable.
- 401 or 403: compare file mount, token purpose, platform instance, bot ID, group ID and adapter-verified actor role. Keep auth bypasses out of a fork.
- Unknown operation result: query its operation ID and compare service observations before any operator-directed retry.
- Local fixture checks: `PYTHONPATH=tests:. python -m unittest discover -s tests`. The snapshot bundles selected tests that run without a QQ account or live AstrBot deployment.

权限不足时核对令牌用途、适配器实例和实际角色。结果不明时按操作 ID 核验，群聊中的受理提示不能代替最终执行回执。
