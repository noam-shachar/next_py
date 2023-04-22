class Animals:
    """ the main structure for defining animals for the zoo"""
    zoo_name = "hayaton"
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger
        self._sound = "mew"

    def get_name(self):
        print(f"The name of the animal is: {self._name}")

    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        self._hunger -= 1

    def talk(self, sound):
        self._sound = sound
        return print(self._sound)


class Dog(Animals):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._type = "Dog"

    def print_type(self):
        return print(self._type)

    def print_name(self):
        return print(self._name)

    def talk(self):
        super().talk("wof wof")


class Cat(Animals):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._type = "Cat"

    def print_type(self):
        return print(self._type)

    def print_name(self):
        return print(self._name)

    def talk(self):
        super().talk("meow")


class Skunk(Animals):
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self._type = "Skunk"
        self._stink_count = stink_count

    def print_type(self):
        return print(self._type)

    def print_name(self):
        return print(self._name)

    def talk(self):
        super().talk("tsssss")


class Unicorn(Animals):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._type = "Unicorn"

    def print_type(self):
        return print(self._type)

    def print_name(self):
        return print(self._name)

    def talk(self):
        super().talk("good day darling")


class Dragon(Animals):
    def __init__(self, name, hunger=0, color="green"):
        super().__init__(name, hunger)
        self._type = "Dragon"
        self._mess = "@#@#@#"
        self._color = color

    def print_type(self):
        return print(self._type)

    def print_name(self):
        return print(self._name)

    def talk(self):
        super().talk("raaawr")

    def breath_fire(self):
        return print(self._mess)


def main():
    if __name__ == '__main__':
        zoo_lst = [Dog("brownie", 10), Cat("Zelda", 3), Skunk("Stinky", 0), Unicorn("Keith", 7), Dragon("Lizzy", 1450)]
        classes = [Dog, Cat, Skunk, Unicorn, Dragon]
        for animal in zoo_lst:
            f"{animal.print_type()}  {animal.print_name()}"
            while animal.is_hungry():
                animal.feed()
            animal.talk()
            if isinstance(animal, Dragon):
                animal.breath_fire()
            #elif ....
        print(Animals.zoo_name)


main()

