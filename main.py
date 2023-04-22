import file1
import file2


def main():
    greeting_msg1 = file1.GreetingCard()
    greeting_msg2 = file2.BirthdayCard()
    greeting_msg1.greeting_msg()
    greeting_msg2.greeting_msg()

if __name__ == '__main__':
    main()

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

