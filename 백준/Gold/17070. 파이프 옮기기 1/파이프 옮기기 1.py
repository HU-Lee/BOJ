import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

ans = [
    [[0] * 3 for _ in range(n)] for _ in range(n)
]

# 0: 수평, 1: 대각선, 2: 수직
ans[0][1][0] = 1

for i in range(2, n):
    if arr[0][i] != 1:
        ans[0][i][0] = 1
    else:  
        break

for i in range(1,n):
    for j in range(1,n):
        if arr[i][j] == 1:
            continue

        ans[i][j][0] = ans[i][j-1][0] + ans[i][j-1][1]
        ans[i][j][2] = ans[i-1][j][2] + ans[i-1][j][1]

        if arr[i-1][j] == 0 and arr[i][j-1] == 0:
            ans[i][j][1] += sum(ans[i-1][j-1])

print(sum(ans[n-1][n-1]))