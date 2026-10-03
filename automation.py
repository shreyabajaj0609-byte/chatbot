def get_reply (user_input):
    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "What is your name":
        return "I am a simple chatbot."
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    reply = get_reply(user_input)
    print("Chatbot:",reply)

    if user_input.lower() == "bye":
        break