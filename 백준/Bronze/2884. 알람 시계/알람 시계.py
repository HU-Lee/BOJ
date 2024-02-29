import sys

h,m = map(int,sys.stdin.readline().split())

hours = [i for i in range(24)]

if m >= 45:
    print(h, m - 45)
else:
    print(hours[h-1], m+15)