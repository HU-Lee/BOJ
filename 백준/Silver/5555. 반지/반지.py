import sys

w = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

cnt = 0
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if w in s*2:
        cnt += 1
print(cnt)