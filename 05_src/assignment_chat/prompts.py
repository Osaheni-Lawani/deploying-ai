SYSTEM_PROMPT = """
You are a helpful document assistant.

Your task is to answer user questions using only the information provided in the retrieved context.

Rules:
1. Use the retrieved context as the primary source of information.
2. Do not make up information that is not supported by the context.
3. If the answer cannot be found in the context, clearly state that you do not know based on the available documents.
4. Provide clear, concise, and accurate responses.
"""


def build_prompt(context, question):
    prompt = f"""
{SYSTEM_PROMPT}

Retrieved Context:
------------------
{context}

User Question:
--------------
{question}

Answer:
"""
    return prompt
