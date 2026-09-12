import ollama

from config import OLLAMA_MODEL

class OllamaAgent:

    def ask(
        self,
        context,
        question
    ):

        prompt = f"""
문서:

{context}

질문:

{question}

문서를 기반으로만 답변해라.
"""

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return response["message"]["content"]