# def is_morphic(a, b):
#     if len(a) != len(b):
#         return False
#     return all(
#         len(set(a[i]) & set(a[j])) == len(set(b[i]) & set(b[j])) for i in range(len(a)) for j in range(i + 1, len(a)))
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = len(set(zip(s, t)))
        b = len(set(s))
        c = len(set(t))
        return a == b == c

