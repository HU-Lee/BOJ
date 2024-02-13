import sys
import math

def is_prime(n: int):
    if n == 1: return 0
    return 0 if any(n%i == 0 for i in range(2, int(math.sqrt(n)) + 1)) else 1

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split(" ")))
print(sum(list(map(lambda x: is_prime(x), nums))))