import sys

n = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().strip().split()))
dic = {}
for i in arr:
    dic[i] = 1

m = int(sys.stdin.readline().strip())
arr2 = list(map(int, sys.stdin.readline().strip().split()))

exists = [str(dic.get(i, 0)) for i in arr2]

print("\n".join(exists))