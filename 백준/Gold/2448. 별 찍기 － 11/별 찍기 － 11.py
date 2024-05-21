import sys

n = int(sys.stdin.readline())

def star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    arr = star(n//2)
    stars = []
    for i in arr:
        stars.append(' '*(n//2) + i + ' '*(n//2))
    for i in arr:
        stars.append(i+' '+i)
    return stars


print('\n'.join(star(n)))