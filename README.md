# Learn Langfuse

Langfuse là nền tảng mã nguồn mở cho **LLM observability**: tracing, monitoring,
debug, đánh giá (evals), quản lý prompt và đo chi phí/latency của ứng dụng AI.

## Cấu trúc

```
learn-langfuse/
├── README.md            # lộ trình học (file này)
├── .env.example         # key Langfuse — copy thành .env
├── pyproject.toml       # deps Python (dùng uv)
├── examples/
│   └── 01_first_trace.py  # trace đầu tiên, không cần API key LLM
└── notes/               # ghi chú khi học
```

## Bước 0 — Chạy Langfuse

**Cách A: Cloud (nhanh nhất)** — đăng ký https://cloud.langfuse.com, tạo project,
lấy Public/Secret key.

**Cách B: Self-host bằng Docker** (chạy ở máy, UI tại http://localhost:3000):

```bash
git clone https://github.com/langfuse/langfuse.git ~/langfuse-server
cd ~/langfuse-server && docker compose up -d
```

> ⚠️ Stack gồm postgres + clickhouse + redis + minio — log container có thể phình
> Docker.raw. Tắt khi không dùng: `docker compose down`.

## Bước 1 — Trace đầu tiên

```bash
cp .env.example .env      # điền key
uv sync
uv run examples/01_first_trace.py
```

Mở UI → **Tracing** → thấy trace `answer_question` với các span con.

## Lộ trình học

| # | Chủ đề | Khái niệm chính |
|---|--------|-----------------|
| 1 | Tracing cơ bản | trace, span, generation, `@observe` |
| 2 | Tích hợp LLM SDK | OpenAI/Anthropic wrapper, LangChain callback |
| 3 | Metadata | `user_id`, `session_id`, tags → lọc & nhóm trace |
| 4 | Chi phí & latency | token usage, model pricing, dashboard |
| 5 | Prompt management | lưu prompt có version, fetch bằng SDK |
| 6 | Scores & evals | chấm điểm thủ công, LLM-as-a-judge |
| 7 | Datasets & experiments | chạy bộ test, so sánh phiên bản prompt/model |

## Tài liệu

- Docs: https://langfuse.com/docs
- GitHub: https://github.com/langfuse/langfuse
- Python SDK: https://langfuse.com/docs/sdk/python
