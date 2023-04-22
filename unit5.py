import winsound
freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }
#notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
#list_notes = notes.split("-")
#final_list = []
#for n in list_notes:
    #t = n.split(",")
    #final_list.append(t)
#for note in final_list:
    #print(freqs[note[0]], int(note[1]))


numbers = iter(list(range(1, 101)))
#for i in numbers:
 #   try:
  #      print(i)
   #     next(numbers)
    #    next(numbers)
    #except StopIteration:
   #     break


bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
import itertools
count = 0
for i in range(16):
    for item in set(itertools.combinations(bills, i)):
        if sum(item) == 100:
            count += 1
#print(count)


class MusicNotes:
    def __init__(self):
        self.tav = -1
        self.oktava = 1
        self.lst_of_notes = [55, 60, 65, 70, 75, 80, 85]

    def __iter__(self):
        return self

    def __next__(self):
        if self.oktava > 5:
            raise StopIteration()
        else:
            self.tav += 1
            if self.tav == 7:
                self.oktava += 1
                self.tav = 0
        return self.lst_of_notes[self.tav] * self.oktava


notes_iter = iter(MusicNotes())
#for freq in notes_iter:
    #print(freq)



def check_id_valid(id_number):
    """check if the id number given is legal
    :param: id number
    :type param: int
    :return: is the id legal
    :rtype: bool
    :Todo: first stage of check - multiplie by 2 if of the nums
    :Todo: second stage - if the multiplie is bigger then 9 add the numbers
    :Todo: third and forth stages - add the new numbers, if the sum divieded by 10 is without leftover good else bad
    """
    list_of_digits = [0] * 9
    new_num = id_number
    for i in range(9):
        list_of_digits[9 - i - 1] = new_num % 10
        new_num = new_num // 10
    sum = 0
    for j in range(len(list_of_digits)):
        list_of_digits[j] = list_of_digits[j] * 2
        if list_of_digits[j] > 9:
            list_of_digits[j] = list_of_digits[j] % 10 + list_of_digits[j] // 10
        sum += list_of_digits[j]
    if sum % 10 == 0:
        return True
    else:
        return False



class IDIterator:
    def __init__(self, id=99999999):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        if self._id > 999999999:
            return StopIteration()
        else:
            while True:
                self._id += 1
                if check_id_valid(self._id):
                    return self._id

def id_generator(id_number):
    while True:
        id_number += 1
        if check_id_valid(id_number):
            yield id_number


def main():
    if __name__ == '__main__':
        id_number = int(input("enter the id num: "))
        iter_or_gen = input("do u want iter or generator? answer iter/gen: ")
        if iter_or_gen == iter:
            id_iter = iter(IDIterator(id_number))
            for i in range(10):
                print(next(id_iter))
        else:
            id_gen = (id_generator(id_number))
            for i in range(10):
                print(next(id_gen))


main()
