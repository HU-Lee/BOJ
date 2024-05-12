import sys
import collections

n,m = map(int,sys.stdin.readline().split())

dic = collections.defaultdict(int)
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if m <= len(word):
        dic[word] += 1

print("\n".join(sorted(list(dic.keys()), key=lambda x: (-dic[x], -len(x), x))))