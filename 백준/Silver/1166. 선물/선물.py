import sys

# print(3.5 // 1.8)

n,l,w,h = map(int,sys.stdin.readline().split())

mi, mx = 0, min(l,w,h)

ans = 0
for _ in range(50):
    mid = (mi+mx)/2
    boxes = (l//mid)*(w//mid)*(h//mid)
    if boxes >= n:
        ans = mid
        mi = mid
    else:
        mx = mid

print(ans)