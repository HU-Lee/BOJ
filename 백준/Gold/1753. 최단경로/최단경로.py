import sys
import collections
import heapq

v,e = map(int,sys.stdin.readline().split())
src = int(sys.stdin.readline())

graph = collections.defaultdict(list)
for _ in range(e):
    i,j,w = map(int,sys.stdin.readline().split())
    graph[i].append((j,w))

INF = 10000000
dis = [INF]*(v+1)
dis[src] = 0

def get_short(src):
    arr = [(0, src)]
    while arr:
        p, d = heapq.heappop(arr)
        for t,w in graph[d]:
            if p + w < dis[t]:
                dis[t] = p + w
                heapq.heappush(arr, (p+w,t))

get_short(src)
for i in dis[1:]:
    print("INF" if i == INF else i)