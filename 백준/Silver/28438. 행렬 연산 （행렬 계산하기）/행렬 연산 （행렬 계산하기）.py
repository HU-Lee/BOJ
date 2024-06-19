import sys
import collections

n,m,q = map(int,sys.stdin.readline().split())

row_change = collections.defaultdict(int)
col_change = collections.defaultdict(int)


for _ in range(q):
    command, x, v = map(int,sys.stdin.readline().split())

    if command == 1:
        row_change[x-1] += v
    else:
        col_change[x-1] += v

matrix = [[row_change[i] + col_change[j] for j in range(m)] for i in range(n)]


for i in range(n):
    print(" ".join(map(str,matrix[i])))