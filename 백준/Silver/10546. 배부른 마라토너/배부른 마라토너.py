import sys

n = int(sys.stdin.readline())

dic = {}
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

for i in range(n-1):
    name = sys.stdin.readline().rstrip()
    if dic[name] > 1:
        dic[name] -= 1
    else:
        del dic[name]
    
for i in dic:
    print(i)