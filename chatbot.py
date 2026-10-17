def chatbot():
    print("=" * 45)
    print("        WELCOME TO CODEALPHA CHATBOT")
    print("=" * 45)
    print("Chatbot: Hello! I am your virtual assistant.")
    print("Chatbot: You can chat with me or type 'bye' to exit.\n")

    while True:
        # User input normalize karna[cite: 2]
        user_input = input("You: ").strip().lower()

        # Rule-based conditions[cite: 2]
        if not user_input:
            print("Chatbot: Please type something so I can respond!")
            continue

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hello there! Hope you are having a wonderful day.")

        elif "how are you" in user_input:
            print("Chatbot: I am doing great, thank you for asking! How about you?")

        elif "your name" in user_input or "who are you" in user_input:
            print("Chatbot: I am a simple rule-based Chatbot built with Python.")

        elif "help" in user_input:
            print("Chatbot: I can answer basic greetings, chat with you, or exit when you type 'bye'.")

        elif "internship" in user_input or "codealpha" in user_input:
            print("Chatbot: CodeAlpha provides great internship opportunities to build projects!")

        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print("Chatbot: Goodbye! It was nice chatting with you. Have a great day ahead!")
            break

        else:
            print("Chatbot: I'm sorry, I don't understand that yet. Try asking 'help' or say 'hello'.")

if __name__ == "__main__":
    chatbot()