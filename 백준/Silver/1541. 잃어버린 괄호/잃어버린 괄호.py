import sys

s = sys.stdin.readline().rstrip()

arr = s.split("-")

ans = 0
for i, x in enumerate(arr):
    if i == 0:
        ans += sum(map(int, x.split("+")))
    else:
        ans -= sum(map(int, x.split("+")))

print(ans)