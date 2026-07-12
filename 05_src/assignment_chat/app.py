import gradio as gr

from rag import answer_question
from memory import ConversationMemory


memory = ConversationMemory()


def chat(question, history):

    previous_history = memory.get_history()

    answer = answer_question(
        question,
        previous_history
    )

    memory.add(
        question,
        answer
    )

    return answer
   


demo = gr.ChatInterface(
    fn=chat,
    title="Document Chat Assistant"
)


if __name__ == "__main__":
    demo.launch()
def chat(message, history):

    return answer_question(
        message,
        history
    )


demo = gr.ChatInterface(
    fn=chat,
    type="messages",
    title="Document Chat Assistant"
)


if __name__ == "__main__":
    demo.launch()
