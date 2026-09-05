# Yotta Docs agent contract

- 跨仓开发与本地进程生命周期遵守相邻 Workspace 的 `workspace/docs/multi-project-development.md`。
- 本仓只拥有公开文档站、用户指南和作者文档，不拥有 Yotta、Registry 或 Hub 的产品实现与生产配置。
- 以当前产品代码、正式 OpenAPI/Schema 和 release 为事实来源；保持各仓独立，不引入跨仓相对源码依赖。
- 保留未提交改动；未经用户明确要求不 push、不改写历史、不绕过 hook。
