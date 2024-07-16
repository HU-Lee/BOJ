import sys

def isValid(n: int):
    for i in range(2, 65):
        cur = n
        arr = []
        while cur > 0:
            arr.append(cur % i)
            cur = cur // i
        if arr == arr[::-1]:
            return True
    return False

n = int(sys.stdin.readline())
for _ in range(n):
    if isValid(int(sys.stdin.readline())):
        print(1)
    else:
        print(0)