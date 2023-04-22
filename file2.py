import file1


class BirthdayCard(file1.GreetingCard):
    def __init__(self, sender_age=0):
        file1.GreetingCard.__init__(self)
        self._sender_age = sender_age

    def greeting_msg(self):
        print(f"Happy birthday, sender's age is {self._sender_age}, recipient is {self._recipient}")