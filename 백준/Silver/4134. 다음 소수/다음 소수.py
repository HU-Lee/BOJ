import sys

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    if n <= 2:
        print(2)
    else:
        while True:
            if is_prime(n):
                print(n)
                break
            n += 1