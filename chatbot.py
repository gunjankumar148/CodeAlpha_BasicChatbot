# Basic Chatbot - CodeAlpha Project

def chatbot():
    print(" Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "what is your name":
            print("Chatbot: I am a simple chatbot created in Python.")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day ")
            break
        else:
            print(" Chatbot: Sorry, I don't understand that.")
chatbot()
