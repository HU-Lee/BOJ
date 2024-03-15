import sys

dic = {
    0: 1
}

def p(n):
    if n < 0:
        return 0
    if n not in dic:
        dic[n] = p(n-1)*n
    return dic[n]

n = int(sys.stdin.readline().strip())

print(p(n))