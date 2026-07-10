import gradio as gr
from rag import answer_question


def chat(message, history):

    return answer_question(
        message,
        history
    )


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
