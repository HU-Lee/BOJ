import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = -1
for x,y in arr:
    if end <= x:
        cnt += 1
        end = y
print(cnt)