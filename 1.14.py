import functools
def num_to_str(number):
    return str(number)
def add_str(number_in_str, next_num_in_str):
    return int(next_num_in_str) + int(number_in_str)
def sum_of_digits(number):
    return functools.reduce(add_str, num_to_str(number))
def main():
    if __name__ == '__main__':
        print(sum_of_digits(113))
main()
