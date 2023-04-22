import functools
def mod4(number):
    return number % 4 == 0
def four_dividers(number):
    return filter(mod4, range(number)[1:])
def main():
    if __name__ == '__main__':
        print(list(four_dividers(9)))
main()