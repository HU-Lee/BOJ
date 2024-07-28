import sys

n = int(sys.stdin.readline())
arr = []

x,y = -1,-1

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    if 2 in row:
        x = i
        y = row.index(2)
    arr.append(row)

target = (x+y) % 2

lena_win = True

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and (i+j) % 2 == target:
            lena_win = False
            break

print("Lena" if lena_win else "Kiriya")

