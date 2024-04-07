import sys

n,m = map(int,sys.stdin.readline().split())

arr = set(map(int,sys.stdin.readline().split()))
arr = list(sorted(arr))

ans = [[x] for x in arr]
for _ in range(m-1):
    ans = [
        x + [y] for x in ans for y in arr
    ]

for i in sorted(ans):
    print(" ".join(map(str,i)))