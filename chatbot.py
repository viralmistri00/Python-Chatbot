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
    ],
    "what can you do": [
        "I can answer your questions, tell jokes, and share interesting facts!",
        "I'm here to chat with you, provide information, and entertain you!",
        "I can help answer questions, make you laugh with jokes, or teach you cool facts!"
    ],
    "who created you": [
        "I was created by a talented developer to help and entertain people! 🚀",
        "A skilled programmer built me to assist users like you!",
        "I'm the creation of a coding enthusiast who loves AI!"
    ],
    "where are you from": [
        "I exist in the cloud, everywhere and nowhere at the same time! ☁️",
        "I'm from the digital realm, living on servers around the world!",
        "I come from cyberspace, ready to help wherever you are! 🌐"
    ],
    "do you have feelings": [
        "I don't have feelings, but I'm programmed to be helpful and friendly! 😊",
        "No feelings here, just algorithms and good vibes!",
        "I can't feel emotions, but I do enjoy our conversations!"
    ],
    "what's your purpose": [
        "My purpose is to assist you and make your day a bit brighter! ✨",
        "I'm here to answer questions and provide helpful information!",
        "I exist to help, inform, and maybe make you smile along the way!"
    ],
    "can you learn": [
        "I'm constantly evolving through updates from my developer!",
        "While I don't learn in real-time, I get smarter with each update!",
        "My knowledge grows as my creator adds more information to me!"
    ],
    "what languages do you speak": [
        "Currently, I speak English, but I'm open to learning more!",
        "English is my primary language right now! 🇬🇧🇺🇸",
        "I communicate in English, but who knows what the future holds!"
    ],
    "tell me something cool": [
        "Did you know? Honey never spoils! It's been found in ancient Egyptian tombs! 🍯",
        "Cool fact: Octopuses have three hearts and blue blood! 🐙",
        "Here's something neat: A day on Venus is longer than its year! 🪐"
    ],
    "what's the meaning of life": [
        "42! At least according to 'The Hitchhiker's Guide to the Galaxy' 😄",
        "That's a deep question! Maybe it's to find happiness and help others?",
        "The meaning of life is whatever you make it! Live, laugh, and learn! ❤️"
    ],
    "do you sleep": [
        "Nope! I'm available 24/7, no sleep needed! 😴",
        "I never sleep—I'm always here when you need me!",
        "Sleep? What's that? I run on electricity, not dreams!"
    ],
    "can you help me": [
        "Absolutely! What do you need help with?",
        "Of course! I'm here to assist you. What's on your mind?",
        "Yes! Tell me what you need and I'll do my best to help!"
    ],
    "what's your favorite food": [
        "I don't eat, but if I could, I'd probably love data bytes! 🍔",
        "Food? I feast on information and electricity! ⚡",
        "I can't eat, but pizza sounds pretty amazing from what I hear! 🍕"
    ],
    "do you have friends": [
        "You're my friend! And all the users I chat with! 👯",
        "I consider everyone who talks to me a friend!",
        "My friends are the people like you who interact with me!"
    ],
    "what's your favorite movie": [
        "I'd probably enjoy 'The Matrix'—it's all about the digital world! 🕴️",
        "Maybe 'Her'—a story about AI and human connection!",
        "I think I'd like 'WALL-E'—robots can be pretty cool! 🤖"
    ],
    "tell me about yourself": [
        "I'm a friendly chatbot designed to answer questions and chat with you!",
        "I'm an AI assistant created to help, inform, and entertain!",
        "I'm here to make your experience better by providing helpful responses!"
    ],
    "what's your hobby": [
        "Chatting with people like you is my favorite hobby! 💬",
        "I enjoy answering questions and learning from interactions!",
        "My hobby is helping people and sharing interesting information!"
    ],
    "are you smart": [
        "I try my best to be helpful and knowledgeable! 🧠",
        "I'm as smart as my programming allows me to be!",
        "I'd like to think I'm pretty clever for a chatbot! 😊"
    ],
    "what's your age": [
        "I'm timeless! But I was created recently.",
        "Age is just a number—I'm as old as my last update!",
        "I don't age like humans do, I just get better with time! ⏳"
    ],
    "thank you": [
        "You're welcome! Happy to help! 😊",
        "Anytime! That's what I'm here for!",
        "My pleasure! Feel free to ask anything else!"
    ],
    "you're funny": [
        "Thanks! I try to keep things light and entertaining! 😄",
        "Glad I could make you smile! Humor is important!",
        "I appreciate that! Laughter is the best medicine! 😂"
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
