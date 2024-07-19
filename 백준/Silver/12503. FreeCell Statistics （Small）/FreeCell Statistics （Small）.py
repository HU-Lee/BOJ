import sys
import math

t = int(sys.stdin.readline())
for x in range(t):
    n, pd, pg = map(int, sys.stdin.readline().split())
    broken = True
    if 0 < pg < 100:
        for i in range(1, n+1):
            if i * pd % 100 == 0:
                broken = False
                break
    else:
        broken = (pd != pg)

    print(f'Case #{x + 1}: {"Broken" if broken else "Possible"}')