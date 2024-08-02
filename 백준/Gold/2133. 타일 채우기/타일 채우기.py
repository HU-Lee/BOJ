import sys
import collections

n = int(sys.stdin.readline())

dic = collections.defaultdict(int)
dic[2] = 3

def dp(n):
    if n < 2:
        return 0
    if n in dic:
        return dic[n]
    if n % 2 == 0:
        # 첫 2칸에 잘리는 경우
        dic[n] = 3 * dp(n - 2)
        # 다음 i칸에 잘리는 경우
        for i in range(4, n + 1, 2):
            dic[n] += 2 * dp(n-i)
        # 안 잘리는 경우
        dic[n] += 2
        return dic[n]
    else:
        return dic[n]

print(dp(n))
