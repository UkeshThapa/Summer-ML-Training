from conversations.conversations import chat_conversation as chat

def mapping(data):

    if "day" in data:
        chat.day()
    
    elif "exit" in data:
        chat.Exit()
