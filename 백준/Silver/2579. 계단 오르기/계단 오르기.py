import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))


dic = {}

# value that steps k-th block at the end
def dp(k):
    if k == 1:
        dic[1] = arr[0]
    elif k == 2:
        dic[2] = arr[0] + arr[1]
    elif k == 3:
        dic[3] = max(arr[0] + arr[2], arr[1] + arr[2])
    elif k not in dic:
        dic[k] = max(
            dp(k-3) + arr[k-2] + arr[k-1],    # when it's 2 blocks in a row
            dp(k-2) + arr[k-1],               # when it's 1 block in a row
        )

    return dic[k]

print(dp(n))