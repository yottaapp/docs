---
id: mcp
title: 连接 MCP
order: 44
---
# 连接 MCP

在 Yotta 的 MCP 设置中开启服务并确认端口。外部客户端使用 Streamable HTTP 地址 `http://127.0.0.1:端口/mcp` 连接；Yotta 必须保持运行。

设置页提供 Codex 注册入口，也可以在兼容客户端中手动填写地址。服务仅监听本机回环地址。

## 常用工具

| 工具 | 用途 |
| --- | --- |
| `catalog_search` / `catalog_describe` | 查询节点和完整节点用法 |
| `workflow_list` / `workflow_inspect` | 列出工作流、按 ID 读取已保存的图 |
| `authoring_context` | 读取当前编辑器、保存状态、工作流完整内容和本机目标列表 |
| `automation_target` | 解析指定目标的名称和画面尺寸 |
| `automation_capture` | 返回目标或屏幕的实际图片及坐标信息 |
| `workflow_create` / `workflow_apply_patch` | 创建工作流、应用修改 |
| `workflow_set_input_value` | 修改已有节点的一个输入 |
| `workflow_compile` / `workflow_run_preview` | 检查工作流及运行准备信息，不执行流程 |
| `run_list` / `run_get` | 查询运行记录与诊断信息 |

## 截图示例

当前编辑器默认目标：

```json
{}
```

指定工作流默认目标：

```json
{"workflowId":"你的工作流 ID"}
```

指定本机目标：

```json
{"slot":"你的目标标识"}
```

整个 Windows 虚拟桌面：

```json
{"screen":true}
```

以上参数均用于 `automation_capture`。先用 `authoring_context` 找到真实标识，不编造 ID。外部客户端和模型需要支持 MCP 图片内容。

外部 MCP 的修改工具直接修改保存的工作流；软件内 AI 提案则先生成候选，接受后才应用。调用外部修改工具前应保存编辑器中的修改。
