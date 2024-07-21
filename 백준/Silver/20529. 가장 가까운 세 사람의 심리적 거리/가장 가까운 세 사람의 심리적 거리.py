import sys

t = int(sys.stdin.readline())

def mbti(x, y, z):
    result = 0
    for i in range(4):
        if x[i] != y[i]:
            result += 1
        if x[i] != z[i]:
            result += 1
        if y[i] != z[i]:
            result += 1

    return result

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().split()

    ans = 12
    if n <= 32:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    ans = min(ans, mbti(arr[i], arr[j], arr[k]))
    else:
        ans = 0

    print(ans)