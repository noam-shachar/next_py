class GreetingCard:
    def __init__(self, _recipient="Dana Ev", _sender="Eyal Ch"):
        self._recipient = _recipient
        self._sender = _sender

    def greeting_msg(self):
        print(f"The sender is {self._sender}, the recipient is {self._recipient}")


