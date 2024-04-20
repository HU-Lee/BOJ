import sys

n,m = map(int,sys.stdin.readline().split())
dic = {}
for _ in range(n):
    group = sys.stdin.readline().rstrip()
    cnt = int(sys.stdin.readline())
    for _ in range(cnt):
        dic[sys.stdin.readline().rstrip()] = group

for _ in range(m):
    word = sys.stdin.readline().rstrip()
    category = int(sys.stdin.readline().strip())

    if category == 1:
        print(dic[word])
    else:
        arr = sorted([key for key in dic if dic[key] == word])
        for a in arr:
            print(a)