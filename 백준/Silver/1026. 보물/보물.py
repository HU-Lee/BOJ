import sys
import heapq

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

arr.sort()
arr2.sort(reverse=True)

sum = 0
for i in range(n):
    sum += arr[i] * arr2[i]

print(sum)