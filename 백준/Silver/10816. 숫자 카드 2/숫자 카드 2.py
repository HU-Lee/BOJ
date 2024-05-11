import sys
import collections

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dic = collections.defaultdict(int)
for x in arr:
    dic[x] += 1

m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = list(map(lambda x: dic[x], arr))

print(" ".join(map(str, arr)))