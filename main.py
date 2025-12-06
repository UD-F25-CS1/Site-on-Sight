from drafter import *
from drafter.llm import *
from dataclasses import dataclass


@dataclass
class State:
    cat:int

set_gemini_server("https://drafter-gemini-proxy.jgn.workers.dev/")

conversation = []

conversation.append(LLMMessage("user", "Hello, Gemini!"))

response = call_gemini(conversation)

def index(state: State) -> Page:
    """Display the chat interface with conversation history."""
    content = [
        f"Chatbot using Gemini",
        "---"
    ]

    # Show conversation history
    if state.conversation:
        for msg in state.conversation:
            if msg.role == "user":
                content.append(f"You: {msg.content}")
            elif msg.role == "assistant":
                content.append(f"Bot: {msg.content}")
        content.append("---")

start_server(State(5))
