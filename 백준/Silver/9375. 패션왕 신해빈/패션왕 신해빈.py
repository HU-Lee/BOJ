import sys
import collections

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    dic = collections.defaultdict(list)
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        dic[b].append(a)
    sum = 1
    for k in dic.keys():
        sum *= len(dic[k]) + 1
    print(sum - 1)