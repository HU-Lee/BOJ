import sys

n,m = map(int,sys.stdin.readline().split())

arr = [0]*n

for _ in range(m):
    i,j,k = map(int,sys.stdin.readline().split())

    for i in range(i-1,j):
        arr[i] = k

print(" ".join(map(str, arr)))