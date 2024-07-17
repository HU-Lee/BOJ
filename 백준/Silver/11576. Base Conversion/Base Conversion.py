import sys

a,b = map(int,sys.stdin.readline().split())

m = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

number = 0
for i, num in enumerate(arr[::-1]):
    number += num*(a**i)

ans = []
while number > 0:
    ans.append(number%b)
    number = number//b

print(' '.join(map(str,ans[::-1])))

