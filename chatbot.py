import random
from datetime im import datetime
# simple chatbot for basic questions


interesting_facts = [
    "Honey never spoils. Archaeologists have found 3,000-year-old honey in Egyptian tombs that was still edible! 🍯",
    "Bananas are berries, but strawberries aren't! 🍌🍓",
    "Octopuses have three hearts and blue blood. 💙💙",
    "A day on Venus is longer than a year on Venus. It rotates very slowly but orbits the Sun faster. 🪐",
    "Sharks existed before trees. Sharks have been around for over 400 million years! 🦈",
    "There are more stars in the universe than grains of sand on Earth. ✨",
    "Wombat poop is cube-shaped. This helps it mark territory without rolling away. 💩",
    "Sloths can hold their breath longer than dolphins. Some sloths can slow their heart rate to survive underwater. 🦥",
    "Butterflies can taste with their feet. 🦋",
    "The Eiffel Tower can be 15 cm taller during summer due to thermal expansion of the metal. 🗼"
]

jokes = [
    "Why did the computer catch a cold? Because it left its Windows open! 🖥️😷",
    "What do you call a fake noodle? An impasta! 🍝😄",
    "Why don't scientists trust atoms? Because they make up everything! ⚛️🤓",
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾🏆",
    "Why was the computer tired when it got home? It had a hard drive! 💻😴",
    "What's a robot's favorite snack? Computer chips! 🤖🍟"
]

chatbot_qa = {
    "hello": [
        "How can I help you?",
        "Hi there! What can I do for you today?",
        "Hello! Need any assistance?"
    ],
    "how are you": [
        "I'm doing great! How about you?",
        "Fantastic, thanks for asking! And you?",
        "I'm well—ready to help you!"
    ],
    "what is your name": [
        "I'm your friendly chatbot! You can call me Chatty 🤖",
        "My name is ChattyBot, ready to serve!",
        "Chatty here. What's up?"
    ],
    "what do you do": [
        "I chat with users, tell jokes and give facts",
        "I'm here to answer your questions and keep you entertained!",
        "I can help you with questions, jokes, and interesting facts!"
    ],
    "what's the current time": [f"{datetime.now().strftime('%H:%M:%S')}"],
    "what's today's date": [f"{datetime.now().strftime('%Y-%m-%d')}"],
    "tell me a joke": jokes,
    "tell me an interesting fact": interesting_facts,
    "what's your favorite color": [
        "I like blue — it reminds me of clear skies and calm code editors. 💙",
        "Green is nice too! So refreshing.",
        "I'm partial to purple—it's creative and mysterious! 💜"
    ],
    "can you help me with a math problem": [
        "Of course! Give me your math question and I'll solve it step by step. ➗",
        "Absolutely! Send your math problem my way.",
        "Sure thing! What's the math problem?"
    ],
    "are you real": [
        "I'm a virtual chatbot, so not exactly real, but I can chat with you! 🤖",
        "I'm just code, but hope I'm helpful!",
        "Real in the digital sense! I exist to help you."
    ],
    "goodbye": [
        "Goodbye! Have a wonderful day! 👋",
        "See you next time!",
        "Bye! Take care.",
        "Until next time! Stay awesome! ✨"
    ]
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    for key in chatbot_qa:
        if key in user_input:
            answers = chatbot_qa[key]
            return random.choice(answers)
    return "the user question isn't recognized and the user should ask another one. 🤔"

# main function to start chat
def chat():
    print(datetime.now().strftime('%H:%M:%S'), "Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print(datetime.now().strftime('%H:%M:%S'), "Chatbot:", chatbot_qa["goodbye"])
            break
        print(datetime.now().strftime('%H:%M:%S'), "Chatbot:", get_response(user_input))

if __name__ == "__main__":
    chat()
