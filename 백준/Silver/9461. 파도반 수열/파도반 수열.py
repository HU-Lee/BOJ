import sys

dic = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2,
}

def p(n):
    if n not in dic:
        dic[n] = p(n-1) + p(n-5)
    return dic[n]

n = int(sys.stdin.readline().strip())

for i in range(n):
    x = int(sys.stdin.readline().strip())
    print(p(x))