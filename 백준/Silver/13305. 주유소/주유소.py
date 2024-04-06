import sys
import heapq

n = int(sys.stdin.readline())

distances = map(int, sys.stdin.readline().split())
prices = list(map(int, sys.stdin.readline().split()))

mi = prices[0]
sum = 0
for idx, dis in enumerate(distances):
    if prices[idx] < mi:
        mi = prices[idx]
    sum += mi * dis

print(sum)
