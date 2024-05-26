import sys

n,m = map(int,sys.stdin.readline().split())

unk1 = set()
unk2 = set()

for _ in range(n):
    unk1.add(sys.stdin.readline().strip())

cnt = 0
for _ in range(m):
    s = sys.stdin.readline().strip()
    if s in unk1:
        cnt += 1
        unk2.add(s)

unk2 = list(unk2)
unk2.sort()

print(cnt)
for i in unk2:
    print(i)