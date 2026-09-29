"""Trace đầu tiên: dùng @observe để ghi lại cây gọi hàm, giả lập 1 lần gọi LLM."""
import time

from dotenv import load_dotenv

load_dotenv()

from langfuse import get_client, observe, propagate_attributes  # noqa: E402

langfuse = get_client()


@observe()
def retrieve_docs(question: str) -> list[str]:
    time.sleep(0.2)  # giả lập truy vấn vector DB
    return ["Langfuse là nền tảng LLM observability mã nguồn mở."]


@observe(as_type="generation")
def fake_llm(prompt: str) -> str:
    time.sleep(0.5)  # giả lập gọi model
    langfuse.update_current_generation(
        model="fake-model",
        usage_details={"input": len(prompt.split()), "output": 12},
    )
    return "Langfuse giúp bạn trace, debug và đánh giá ứng dụng LLM."


@observe()
def answer_question(question: str) -> str:
    # v4: gắn user_id/tags cho trace bằng propagate_attributes
    with propagate_attributes(user_id="learner", tags=["lesson-1"]):
        docs = retrieve_docs(question)
        prompt = f"Context: {docs}\nQuestion: {question}"
        return fake_llm(prompt)


if __name__ == "__main__":
    print(answer_question("Langfuse là gì?"))
    langfuse.flush()  # script ngắn: đẩy dữ liệu trước khi thoát
