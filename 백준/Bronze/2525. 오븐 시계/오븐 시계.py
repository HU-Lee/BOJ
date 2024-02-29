import sys

h,m = map(int,sys.stdin.readline().split())

mins = int(sys.stdin.readline().strip())

hours = [i for i in range(24)]

plus_h = (m+mins)//60
print(hours[(h+plus_h)%24], (m+mins)%60)
