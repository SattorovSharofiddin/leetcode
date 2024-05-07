from functools import reduce


def test_fun(l: list[int]):
    for i in list(l):
        if l.count(i) == 1:
            return i


l = [3, 4, 4, 6, 3]
print(test_fun(l))
