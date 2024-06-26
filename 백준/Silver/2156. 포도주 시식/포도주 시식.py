import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

if n <= 2:
    print(sum(arr))
else:    
    # n까지의 dp
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[1] + arr[2], arr[0] + arr[2], arr[0] + arr[1])

    for i in range(3, n):
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i], dp[i - 1])
            
    print(max(dp))