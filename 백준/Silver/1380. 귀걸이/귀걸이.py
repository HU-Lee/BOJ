import sys

cnt = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    girls = []
    for _ in range(n):
        girls.append(sys.stdin.readline().strip())
    dic = {}
    for _ in range(2*n-1):
        idx, val = sys.stdin.readline().split()
        idx = int(idx)
        key = girls[idx-1]
        if key in dic:
            del dic[key]
        else:
            dic[key] = val

    print(cnt, list(dic.keys())[0])
    cnt += 1