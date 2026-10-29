"""Chat history: a plain Python list of LangChain messages."""

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


def create_history():
    """Start a new history list with a short session note."""
    return [SystemMessage(content="A new chat session has started.")]


def add_interaction(history, question, answer):
    """Save one question/answer pair to the history."""
    history.append(HumanMessage(content=question))
    history.append(AIMessage(content=answer))
