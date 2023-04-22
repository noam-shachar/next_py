import functools
def intersection(list_1, list_2):
    return list(set(filter(lambda x: str(x) in str(list_2), list_1)))
print(intersection([1, 2, 3, 4], [8, 3, 9, 3, 4]))

