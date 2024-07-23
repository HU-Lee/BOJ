import sys

n,m = map(int,sys.stdin.readline().split())
a = []

for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))

m,k = map(int,sys.stdin.readline().split())
b = []
for _ in range(m):
    b.append(list(map(int,sys.stdin.readline().split())))

k = len(b[0])
for i in range(n):
    for j in range(k):
        print(sum(a[i][x]*b[x][j] for x in range(m)),end=' ')
    print()