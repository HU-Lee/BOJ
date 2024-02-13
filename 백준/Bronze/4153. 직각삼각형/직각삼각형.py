import sys
import math

while True:
    a,b,c = sorted(list(map(int, sys.stdin.readline().split(" "))))
    if a == 0: break
    print("right" if a**2+b**2 == c**2 else "wrong")