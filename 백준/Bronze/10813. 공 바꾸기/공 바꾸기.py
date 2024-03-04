import sys

n,m = map(int,sys.stdin.readline().split())

arr = [i + 1 for i in range(n)]

for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())

    tmp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = tmp

print(" ".join(map(str, arr)))