import gradio as gr
from retrievers import RetrieverSelector

selector = RetrieverSelector()

def chatbot_response(message, history):
    for chunk in selector.call(message,history):
        yield chunk

def build_chatbot_interface():
    """Builds and launches the Gradio chatbot interface."""

    iface = gr.ChatInterface(fn=
        chatbot_response,
        textbox=gr.Textbox(label="Enter your message", placeholder="Type here..."),
        title="Warhammer 40k Rules Chatbot",
        description="Ask me about Warhammer 40k rules!"
    )
    return iface

if __name__ == "__main__":
    iface = build_chatbot_interface()
    iface.launch()
