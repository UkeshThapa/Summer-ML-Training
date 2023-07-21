from datetime import *
import random
import conversations.constant as c

now = datetime.now()


class chat_conversation:
    def greeting():
        hour = int(now.hour)
        if hour>=0 and hour<12:
            print("Good Morning!")

        elif hour>=12 and hour<18:
            print("Good Afternoon!")
        else:
            print("Good evening!")

        print(random.choice(c.greeting))

    def day():
        days = now.strftime("%A, %B %d")
        print(f"Today is {days}")

    def Exit():
        print(random.choice(c.close))
        exit()