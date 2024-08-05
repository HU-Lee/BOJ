import sys
import collections

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cnt = collections.defaultdict(int)
for i in arr: 
    cnt[i] += 1

compressed = {}
acc = 0
for key in sorted(cnt.keys()):
    compressed[key] = acc
    acc += 1

ans = list(map(lambda x: str(compressed[x]), arr))
print(' '.join(ans))