import sys
import collections

c = int(sys.stdin.readline())
s = int(sys.stdin.readline())

dic = collections.defaultdict(list)
for _ in range(s):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [False] * (c + 1)
visited[1] = True

queue = collections.deque([1])
while queue:
    x = queue.popleft()
    for i in dic[x]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)

print(len(list(filter(lambda x: x, visited))) - 1)