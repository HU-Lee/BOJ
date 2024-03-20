import sys
import math

def check(n):
    arr = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            arr.append(i)
            if i != n // i:
                arr.append(n // i)
    if sum(arr) == n:
        print(n, "=", " + ".join([str(x) for x in sorted(arr)]))
    else:
        print(n, "is NOT perfect.")

while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:
        break
    check(n)
    