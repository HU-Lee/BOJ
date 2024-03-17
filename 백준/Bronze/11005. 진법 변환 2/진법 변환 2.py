import sys

n, b = map(int, sys.stdin.readline().split())

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s = ""

while n > 0:
    x = n % b
    if x >= 10:
        x = alphabets[x - 10]
    s = str(x) + s
    n = n // b

print(s)