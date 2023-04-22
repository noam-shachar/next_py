import functools
def is_prime(number):
    return True if len(list(filter(lambda x: False if number % x != 0 else True,
                            [i for i in range(2, round(number / 2) + 1)]))) == 0 else False
#print(is_prime(56))

def is_funny(string):
    return True if len(list(filter(lambda char: True if char == 'h' or char == 'a' else False,
                            [char for char in string]))) == len(string) else False
    #for char in string:
     #   if char != 'h' and char != 'a':
      #      return False
    #return True
#print(is_funny("aaaahhhhahahahd"))

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
def shift2(password):
    return "".join(list(map(lambda char: chr(ord(char) + 2) if char.isalpha() else char, [char for char in password])))
print(shift2(password))