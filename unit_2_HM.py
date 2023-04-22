class Oktopus:
    count_animal = 0
    def __init__(self, name="noam", age=0):
        self._name = name
        self._age = age
        Oktopus.count_animal += 1
    def set_name(self, name):
        self._name = name
    def get_name(self):
        print(self._name)
    def birthday(self):
        self._age += 1

    def get_age(self):
        print(f"{self._name} age is: {self._age}")


#def main():
    #if __name__ == "__main__":
        okti = Oktopus("okti", 5)
        peri = Oktopus()
        peri.birthday()
        peri.set_name("peri")
        peri.get_name()
        peri.get_age()
        okti.get_age()
        print(f"number of animals: {Oktopus.count_animal}")


#main()

class Pixel:
    def __init__(self, x=0, y=0, red=0, blue=0, green=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue
        self._avg = 0

    def set_cords(self, x=0, y=0):
        self._x = x
        self._y = y

    def set_grayscale(self):
        self._avg = round((self._red + self._green + self._green) / 3)
        self._red = self._avg
        self._green = self._avg
        self._blue = self._avg

    def print_pixel_info(self):
        print(f"X: {self._x} Y: {self._y}, color: ({self._red},{self._green},{self._blue})")

#def main():
    #if __name__ == '__main__':
      #  p = Pixel(5, 6, 250)
     #   p.print_pixel_info()
     #   p.set_grayscale()
     #   p.print_pixel_info()


#main()


class BigThing:
    """ the class measeurs the object size and return if it is big"""
    def __init__(self, something=1):
        self._object = something
        self._type = type(something)

    def size(self):
        if self._type == int:
            self._size = self._object
        else:
            self._size = len(self._object)
        return self._size


class BigCat(BigThing):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    def size(self):
        if self._size > 15:
            return "fat"
        else:
            return "not fat"


def main():
    if __name__ == '__main__':
        my_thing = BigThing("balloon")
        print(my_thing.size())
        cutie = BigCat("mitzy", 22)
        print(cutie.size())


main()
