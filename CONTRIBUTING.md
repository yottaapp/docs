# Yotta 文档维护

本仓库是 Yotta 公开文档的唯一内容与打包来源。用户指南在 [content/index.md](content/index.md)，中文在 `content/zh/`，英文在 `content/en/`，图片共用 `content/assets/`。产品仓 `yotta/docs/` 继续保存实现相关的架构、版本和开发说明。

## 本地打包与月离文档

需要 Python 3.10+；在本仓执行：

```powershell
./scripts/docs.ps1
./scripts/docs.ps1 -Action Preflight -Collection yotta
./scripts/docs.ps1 -Action Publish -Collection yotta
```

默认生成 `artifacts/docs.zip`。预检和发布使用环境变量 `YUELI_DOCS_TOKEN`，令牌需具有月离文档导入权限。发布默认 upsert，保留包中未出现的页面；确认超时后使用发布脚本的 status 命令查询返回的 batch ID。

脚本已从全局 yueli-docs-publish skill 复制到本仓，仅使用 Python 标准库。正文、截图和脚本均不依赖相邻产品 checkout，也不依赖个人 `.codex` 路径。

## 内容格式

根 `content/docs.json` 声明 `zh-CN`、`en-US`。每篇 Markdown 使用 title、id、order 等 frontmatter；对应翻译使用同一 id，同一语言内不得重复。图片和页面使用包内相对链接。

当前中文 26 篇、英文 23 篇；新 AI 提案、MCP、截图章节先提供中文。现有 5 张截图来自 4.0.0-alpha.2；不要把它们标为最新界面。

## GitHub Actions

PR、main 更新和手动 dispatch 会校验并生成可下载的 yotta-documentation artifact。推送 docs-* 标签时，工作流在本仓创建 Release，附带 docs.zip、release.json 和 SHA256SUMS；已有 Release 不覆盖。维护者应在标签发布前更新 release.json 中对应的产品版本。

月离文档后台的项目同步应绑定 yottaapp/docs、附件 docs.zip 和目标文档集。软件仓库不再自行打包另一份文档。文件迁移不意味着已经推送仓库、发布 Release 或上传文档站。

## 迁移来源

原指南来自 yuelioi/yotta 提交 15062bb0d98323ffebd2c983aeb6fb7eb01a92e2 中的 docs/user-guide/，历史仍保留在原仓，可沿原路径查询。其 46 篇中英文指南和 5 张图片完整迁入；图片逐一核对 Git blob 一致。

2026-09-09 的 AI/MCP/截图新增内容及与旧教程的合并来自同日未提交工作树，不能用上述提交冒充它们的已发布来源。中间的 yotta/user-docs/ 已撤销；当前内容直接维护在本仓 content/。旧 source_id 已转换为文档导入支持的 id。
