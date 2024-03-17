import sys

n, b = sys.stdin.readline().split()
b = int(b)

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

mul = 1
sum = 0
for i in reversed(n):
    if i in "0123456789":
        x = int(i)
    else:
        x = alphabets.index(i) + 10
    sum += mul*x
    mul *= b

print(sum)