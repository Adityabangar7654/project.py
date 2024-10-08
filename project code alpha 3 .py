import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you today?", ]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"what is your name?",
        ["I am a simple chatbot created to assist you!", "You can call me Chatbot."]
    ],
    [
        r"how are you?",
        ["I'm doing great! How about you?", "I'm good, thanks for asking! How can I help you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay!", "No worries!", "Don't mention it."]
    ],
    [
        r"I (.*) good",
        ["That's great to hear!", "I'm happy to know that!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Glad to assist you!"]
    ],
    [
        r"quit",
        ["Goodbye! It was nice talking to you. Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand, can you rephrase that?", "Can you please explain more?"]
    ],
]

# Reflections for some basic substitutions
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "me": "you"
}

# Create Chatbot using NLTK
def chatbot():
    print("Hi! I am a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
