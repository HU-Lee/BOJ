import sys

n,b = map(int,sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

dic = {
    1: arr
}

def matrix_mul(mat1, mat2):
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += mat1[i][k] * mat2[k][j]
            temp[i][j] %= 1000
    return temp

def dp(x):
    if x in dic:
        return dic[x]
    else:
        if x%2 == 0:
            dic[x] = matrix_mul(dp(x//2),dp(x//2))
        else:
            temp = matrix_mul(dp(x//2),dp(x//2))
            dic[x] = matrix_mul(temp,arr)
        return dic[x]

ans = dp(b)
for i in range(n):
    print(" ".join(map(lambda x: str(x%1000),ans[i])))