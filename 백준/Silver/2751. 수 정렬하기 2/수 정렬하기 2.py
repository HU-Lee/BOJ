import sys
import heapq

n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    heapq.heappush(arr, x)

while arr:
    print(heapq.heappop(arr))