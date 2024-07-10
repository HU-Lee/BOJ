import sys

n,m = map(int,sys.stdin.readline().split())

dic = {}
for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    dic[i] = name
    dic[name] = i

for j in range(m):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(dic[int(question)])
    else:
        print(dic[question])