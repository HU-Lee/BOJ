import sys

x = sys.stdin.readline().rstrip()
y = sys.stdin.readline().rstrip()

l_x = len(x)
l_y = len(y)

dp = [[0] * (l_y + 1) for _ in range(l_x + 1)]

# 문자열 계산이 오래 걸리므로 숫자로 DP
for i in range(l_x):
    for j in range(l_y):
        if x[i] == y[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j+1], dp[i+1][j])

# 역추적
n = dp[l_x][l_y]
print(n)
if n > 0:
    i = l_x
    j = l_y
    s = ''
    while n > 0:
        if x[i - 1] == y[j - 1]:
            s += x[i - 1]
            i -= 1
            j -= 1
            n -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print(s[::-1])