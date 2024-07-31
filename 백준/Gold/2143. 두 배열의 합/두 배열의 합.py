import sys
import collections

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

parts1 = collections.defaultdict(int)
for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += arr1[j]
        parts1[tmp] += 1

ans = 0

# parts2 = collections.defaultdict(int)
# 2번째도 dictionary에 데이터 저장하면 메모리 초과

for i in range(m):
    tmp = 0
    for j in range(i, m):
        tmp += arr2[j]
        ans += parts1[t-tmp]

print(ans)