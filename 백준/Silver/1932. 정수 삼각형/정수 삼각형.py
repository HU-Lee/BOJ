import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dic = {
    (0,0): arr[0][0]
}

def dp(i, j):
    if (i, j) in dic:
        return dic[(i, j)]
    if i < j or j < 0:
        dic[(i, j)] = 0
    else:
        dic[(i, j)] = max(dp(i-1, j), dp(i-1, j-1)) + arr[i][j]
    return dic[(i, j)]

print(max(dp(n-1, i) for i in range(n)))