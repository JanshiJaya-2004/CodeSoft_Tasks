def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there! How can I help you?"
    elif "weather" in user_input.lower():
        return "I can't predict weather yet, but I’m learning!"
    else:
        return "Sorry, I don't understand that."

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    print("Bot:", chatbot_response(user))
