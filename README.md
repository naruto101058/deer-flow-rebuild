# Deer Flow Rebuild

本项目是 Deer Flow 系统的后端重构版本。基于现代化的 Python 异步 Web 框架 FastAPI 构建，旨在提供稳定、高性能且易于扩展的 API 服务。

## 🎯 项目目标

- 重构并优化原有后端的业务逻辑与数据流转。
- 提供高并发、低延迟的 API 接口支持。
- 建立规范的自动化测试和现代化依赖管理流程（基于 `uv` 工具）。

## 🛠️ 安装依赖

本项目使用极速的 Python 包管理工具 [uv](https://github.com/astral-sh/uv) 进行环境和依赖管理。

**注意：由于项目的配置文件位于后端目录中，因此安装、启动和测试命令都需要在 `backend/` 目录下执行。**

执行以下命令，严格按照已提交的锁文件进行环境安装：

```bash
# 从仓库根目录进入后端
cd backend
uv sync --locked
```

*(备注：`--locked` 参数要求 `uv` 严格按照已提交的 `uv.lock` 锁文件进行安装，防止因依赖包自动升级导致不同电脑上的环境不一致。如果你需要手动补全依赖，参考命令：核心包 `uv add 'fastapi==0.136.1' 'uvicorn[standard]==0.46.0'`，开发包 `uv add --dev 'pytest==9.0.3' 'httpx==0.28.1'`)*

## 🚀 启动服务

确保当前在 `backend/` 目录下，通过以下命令启动后端服务，并开启热重载模式（修改代码后无需手动重启服务）：

```bash
uv run uvicorn backend.api:app --host 127.0.0.1 --port 8101 --reload
```

启动成功后，你可以在浏览器中访问：
- **健康检查接口**: [http://127.0.0.1:8101/health](http://127.0.0.1:8101/health)
- **交互式 API 文档 (Swagger UI)**: [http://127.0.0.1:8101/docs](http://127.0.0.1:8101/docs)

## 🧪 运行测试

本项目使用 `pytest` 作为自动化测试框架。提交代码前请务必运行测试以保证代码质量。

确保当前在 `backend/` 目录下，以“安静模式”（过滤多余日志，仅输出核心结果）运行所有的自动化测试：

```bash
uv run python -m pytest -q
```
