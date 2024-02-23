import sys
import re

n,m = map(int,sys.stdin.readline().split())

arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    add_arr = list(map(int,sys.stdin.readline().split()))
    arr[i] = [str(arr[i][x] + add_arr[x]) for x in range(len(add_arr))]

for i in range(n):
    print(" ".join(arr[i]))