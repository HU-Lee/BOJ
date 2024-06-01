import sys

n = int(sys.stdin.readline())
dp = [0,1,1,1,1,1,1,1,1,1]
for i in range(2, n + 1):
    new_dp = [0,0,0,0,0,0,0,0,0,0]
    for j in range(10):
        if j == 0:
            new_dp[j] = dp[j + 1] % 1000000000
        elif j == 9:
            new_dp[j] = dp[j - 1] % 1000000000
        else:
            new_dp[j] = (dp[j - 1] + dp[j + 1]) % 1000000000

    dp = new_dp

print(sum(dp) % 1000000000)
