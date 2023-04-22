import functools

with open(r"C:\Users\עמית שחר\PycharmProjects\next_py\names_database.py", "r") as names_file:
    def longest_name(file):
        return functools.reduce(lambda name1, name2: name1 if len(name1) > len(name2) else name2, [name[:-2] if
                name[-2] == "\\" else name for name in file.readlines()])
    print(longest_name(names_file))
    print(names_file.readlines())
    def sum_of_letters(file):
        return functools.reduce(lambda name1, name2: sum(name1 + name2), [name[:-2] if
                name[-2] == "\\" else name for name in file.readlines()])
    print(sum_of_letters(names_file))
    print(names_file.readlines())
