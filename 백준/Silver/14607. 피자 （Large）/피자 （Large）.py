import sys
import collections

n = int(sys.stdin.readline())
dic = collections.defaultdict(int)
dic[1] = 0

def dfs(n):
    if n in dic:
        return dic[n]
    x = n // 2
    dic[n] = dfs(x) + dfs(n - x) + x*(n-x)
    return dic[n]

print(dfs(n))