import sys

s = sys.stdin.readline().strip()
t = 'UCPC'

arr = []
for x in s:
    l = len(arr)
    if l == 4:
        break
    if x == t[l]:
        arr.append(x)

print('I love UCPC' if len(arr) == 4 else 'I hate UCPC')