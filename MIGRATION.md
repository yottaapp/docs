# Documentation migration

## 第一批候选

- `yotta/docs/user-guide/`：公开用户指南与图片资源；
- 插件协议和 SDK 的面向作者说明；
- Hub 上传、下载、发布与账户使用说明；
- Registry 的发布、依赖、签名和审核说明。

## 留在 Yotta

- `docs/architecture/`；
- `docs/compatibility.md`、`docs/platform-support.md` 和 `docs/reference/cli.md`；
- `flightdeck/knowledge/`；
- 被 Task、测试、schema 或生成器直接引用的说明。

迁移前逐项核对生产代码和正式契约，不用旧文档自证当前行为。
