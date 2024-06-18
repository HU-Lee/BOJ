import sys

n,m = map(int,sys.stdin.readline().split())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

if m > n:
    n,m = m,n

print(n*m//gcd(n,m))