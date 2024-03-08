import sys

mx = 0
i,j = 0,0
for x in range(9):
    arr = list(map(int, sys.stdin.readline().split()))
    for y, num in enumerate(arr):
        if mx < num:
            mx,i,j = num,x,y

print(mx)
print(i+1,j+1)


