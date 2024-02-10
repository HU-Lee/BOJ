import sys

arr = [i for i in range(1, 31)]

for i in range(28): 
    n = int(sys.stdin.readline())
    arr = [i for i in arr if i != n]

for i in arr:
    print(i)