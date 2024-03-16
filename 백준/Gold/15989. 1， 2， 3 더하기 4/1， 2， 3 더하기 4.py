import sys

sys.setrecursionlimit(5000000)

dic = {
    (1,1): 1,
    (1,2): 0,
    (1,3): 0,
    (2,1): 1,
    (2,2): 1,
    (2,3): 0,
    (3,1): 1,
    (3,2): 1,
    (3,3): 1
}

# 최대 y로 x를 나타내는 조합 개수
def dp(x, y):
    if (x, y) not in dic:
        if y == 1:
            dic[(x, y)] = 1
        elif y == 2:
            dic[(x, y)] = dp(x-2, 2) + dp(x-2, 1)
        else:
            dic[(x, y)] = dp(x-3, 3) + dp(x-3, 2) + dp(x-3, 1)
    return dic[(x, y)]

n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    print(dp(x, 3) + dp(x, 2) + dp(x, 1))