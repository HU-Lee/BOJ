import sys
import collections

t = int(sys.stdin.readline().rstrip())

arr = [""]
for _ in range(4):
    letters = list(set(sys.stdin.readline().rstrip()))
    arr = [a + b for a in arr for b in letters]

for _ in range(t):
    target = sys.stdin.readline().rstrip()
    c_target = collections.Counter(target)
    can_spell = False
    for s in arr:
        c_s = collections.Counter(s)
        if all(c_target[k] <= c_s[k] for k in c_target):
            can_spell = True
            break
    print("YES" if can_spell else "NO")
    
