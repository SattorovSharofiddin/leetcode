hp = {}
nums = [0, 4, 5, 0, 3, 6]
k = 3


def fun(nums, k):
    for idx, element in enumerate(nums):
        if element in hp.keys() and abs(hp[element] - idx) <= k:
            return True
        hp[element] = idx
    return False


print(fun(nums, k))
