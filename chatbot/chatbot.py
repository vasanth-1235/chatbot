def get_response(user_input):
    # Convert the user input to lower case for case insensitive matching
    user_input = user_input.lower()

    # Define responses based on user input
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm a chatbot, so I don't have feelings, but I'm here to help you!"
    elif "your name" in user_input:
        return "I'm ChatGPT, your virtual assistant."
    elif "what can you do" in user_input:
        return "I can chat with you and provide information based on predefined rules. Try asking me about the weather, time, or some basic information."
    elif "weather" in user_input:
        return "I'm sorry, I can't provide real-time weather updates right now."
    elif "time" in user_input:
        return "I'm sorry, I can't tell you the current time."
    elif "exit" in user_input or "quit" in user_input or "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

def main():
    print("Hello! I'm ChatGPT, your virtual assistant. Type 'exit', 'quit', or 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("ChatGPT: " + response)
        if user_input.lower() in ["exit", "quit", "bye"]:
            break

if __name__ == "__main__":
    main()
