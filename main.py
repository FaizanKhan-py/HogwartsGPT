"""WizardChat AI - a terminal Harry Potter chatbot built with LangChain."""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from chat_history import add_interaction, create_history
from prompts import prompt

load_dotenv()  # loads OPENAI_API_KEY from .env

EXIT_WORDS = {"exit", "quit"}

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    base_url="https://mychatbot2.openai.azure.com/openai/v1",
)

# prompt | llm  -> fills in the template, then sends it to the model
chain = prompt | llm


def main():
    chat_history = create_history()

    print("=" * 50)
    print("  WizardChat AI - Your Harry Potter Guide")
    print("  Type 'exit' or 'quit' to leave.")
    print("=" * 50)

    while True:
        question = input("\nYou: ")

        if question.lower() in EXIT_WORDS:
            print("WizardChat AI: Mischief managed! Goodbye!")
            break

        response = chain.invoke({"chat_history": chat_history, "question": question})
        answer = response.content
        print(f"\nWizardChat AI: {answer}")

        add_interaction(chat_history, question, answer)


if __name__ == "__main__":
    main()