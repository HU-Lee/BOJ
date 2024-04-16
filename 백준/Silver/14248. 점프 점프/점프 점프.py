import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
s = int(sys.stdin.readline())

visited = [False] * (n)
q = [s-1]
visited[s-1] = True

while q:
    x = q.pop(0)
    for i in [x-arr[x], x+arr[x]]:
        if 0 <= i < n and not visited[i]:
            visited[i] = True
            q.append(i)

print(len(list(filter(lambda x: x, visited))))