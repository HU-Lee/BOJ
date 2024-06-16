import sys

n,m = map(int,sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

ans = 64
for i in range(n-7):
    for j in range(m-7):
        cw,cb = 0,0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) % 2 == 0:
                    if arr[k][l] == 'B':
                        cw += 1
                    else:
                        cb += 1
                else:
                    if arr[k][l] == 'B':
                        cb += 1
                    else:
                        cw += 1
        ans = min(ans,min(cw,cb))

print(ans)