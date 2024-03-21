import sys

n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(n):
    l = len(
        [x for x in arr if x[0] > arr[i][0] and x[1] > arr[i][1]]
    )
    print(l + 1, end=" ")