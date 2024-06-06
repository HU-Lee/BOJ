import sys
import math

t = int(sys.stdin.readline()) 

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    g = math.gcd(a,b)
    print(a*b//g, g)