# URL: https://leetcode.com/problems/add-binary/
a = '11'
b = '1'


def add_binary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
