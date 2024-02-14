import sys

a,b,c = list(map(int, sys.stdin.readline().split(" ")))

def get_mod(a,b,c):
    if b == 1:
        return a%c
    else:
        if b % 2 == 0:
            return get_mod(a, b//2, c)**2%c
        else:
            return get_mod(a, b//2, c)**2*a%c
        
print(get_mod(a,b,c))