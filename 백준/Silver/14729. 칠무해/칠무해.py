import sys
import heapq

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    heapq.heappush(arr, float(sys.stdin.readline().rstrip()))

for _ in range(7):
    x = heapq.heappop(arr)
    print('{:.3f}'.format(x))