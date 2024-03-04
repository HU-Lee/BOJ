import sys

n,m = map(int,sys.stdin.readline().split())

arr = [i + 1 for i in range(n)]

for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())

    arr[i-1:j] = arr[i-1:j][::-1]

print(" ".join(map(str, arr)))