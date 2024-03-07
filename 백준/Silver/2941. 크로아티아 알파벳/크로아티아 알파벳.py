import sys

s = sys.stdin.readline().strip()

words = sorted(['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='], key=len, reverse=True)

for word in words:
    s = s.replace(word, 'a')

print(len(s))