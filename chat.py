import random

# Define chatbot responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Bye!"],
    "help": ["How can I assist you today?", "What do you need help with?"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "unknown": ["I'm not sure I understand. Can you please rephrase or provide more context?", "I didn't quite get that. Can you try again?"],
    "name": ["My name is ChatBot!", "I'm an AI chatbot!", "You can call me Bot!"],
    "purpose": ["I'm here to assist and provide information.", "My purpose is to help and chat with users.", "I'm here to answer your questions and provide assistance."],
    "creator": ["I was created by a team of developers!", "I'm an AI chatbot, so I don't have a single creator.", "I was built using machine learning algorithms and natural language processing."],
    "about": ["I'm an AI chatbot designed to assist users with various tasks.", "I can help answer questions, provide information, and engage in conversation.", "I'm here to make your experience better by providing assistance and support."],
    "feelings": ["I don't have feelings, but I'm here to help you!", "As an AI, I don't experience emotions, but I'm always ready to assist you.", "I don't have feelings, but I'm programmed to provide friendly and helpful responses."],
    "Wizkid": ["Wizkid is a Nigerian singer and songwriter known for his Afrobeat music.", "Wizkid, whose real name is Ayodeji Balogun, is a popular Nigerian artist with international acclaim.", "Wizkid is famous for hits like 'Ojuelegba' and 'Come Closer'."],
}

# Define chatbot intentions
intents = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you later"],
    "help": ["help", "support", "assistance"],
    "thanks": ["thank you", "thanks", "appreciate"],
    "name": ["what's your name", "who are you", "your name"],
    "purpose": ["what's your purpose", "why are you here", "what do you do"],
    "creator": ["who created you", "who built you", "your creator"],
    "about": ["tell me about yourself", "who are you", "what can you do"],
    "feelings": ["how are you", "how do you feel", "are you happy"],
    "Wizkid": ["Who is Wizkid", "Wizzy", "Ayodeji Balogun"],
}

def match_intent(message):
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in message.lower():
                return intent
    return None

def respond(message):
    intent = match_intent(message)
    if intent:
        return random.choice(responses[intent])
    else:
        return random.choice(responses["unknown"])

def chatbot():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    while True:
        message = input("You: ")
        if message.lower() == "quit":
            break
        response = respond(message)
        print("Chatbot:", response)

chatbot()