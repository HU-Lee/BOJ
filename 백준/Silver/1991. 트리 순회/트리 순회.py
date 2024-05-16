import sys
import collections

lefts = collections.defaultdict(None)
rights = collections.defaultdict(None)

n = int(sys.stdin.readline())
for _ in range(n):
    x, l, r = sys.stdin.readline().rstrip().split()
    if l != '.':
        lefts[x] = l
    if r != '.':
        rights[x] = r

def front(x):
    s = x
    if x in lefts:
        s += front(lefts[x])
    if x in rights:
        s += front(rights[x])
    return s

def middle(x):
    s = x
    if x in lefts:
        s = middle(lefts[x]) + s
    if x in rights:
        s += middle(rights[x])
    return s

def back(x):
    s = x
    if x in rights:
        s = back(rights[x]) + s
    if x in lefts:
        s = back(lefts[x]) + s
    return s

print(front('A'))
print(middle('A'))
print(back('A'))