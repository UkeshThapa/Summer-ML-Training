from conversations.conversations import chat_conversation
from conversations.mapping import mapping as mp_func


def main():
    chat_conversation.greeting()
    while True:
        data = input(f'yukesh: ')
        mp_func(data)
    

if __name__ == "__main__":
    main()