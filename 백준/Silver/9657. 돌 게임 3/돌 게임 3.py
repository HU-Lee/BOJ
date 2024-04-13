import sys

win = {
    1: "SK", 2: "CY", 3: "SK", 4: "SK"
}

def dp(n):
    if n in win:
        return win[n]
    else:
        if "CY" in [dp(n-1), dp(n-3), dp(n-4)]:
            win[n] = "SK"
        else:
            win[n] = "CY"
        return win[n]
        
n = int(sys.stdin.readline())
print(dp(n))