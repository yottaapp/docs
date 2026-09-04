# Yotta Documentation

本仓拥有 Yotta 的公开、可发布文档站点内容，包括用户指南、插件作者指南、Registry 使用指南和跨产品说明。

## 与产品仓文档的分工

- 本仓：面向用户和插件作者的公开文档及其站点实现。
- `yotta/docs`：与特定代码版本一起演进的产品模型、架构、兼容、安全和 CLI reference。
- `yotta/flightdeck/knowledge`：修改产品源码时使用的仓库内开发指南。
- 各仓 schema、测试和生成契约仍是最终事实来源。

首次迁移应保留 Git 历史，并建立文档版本与对应 Yotta release 的关系；在迁移完成前不从 `yotta` 删除原内容。
