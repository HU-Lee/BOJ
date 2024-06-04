import sys

arr = []
for _ in range(19):
    arr.append(list(map(int, sys.stdin.readline().split())))

def stone(h, w):
    if 0 <= h < 19 and 0 <= w < 19:
        return arr[h][w]
    return -1

def check(h,w):
    val = stone(h, w)
    return (all(stone(h+i, w) == val for i in range(5)) and stone(h+5, w) != val and stone(h-1, w) != val) \
        or (all(stone(h, w+i) == val for i in range(5)) and stone(h, w+5) != val and stone(h, w-1) != val) \
        or (all(stone(h-i, w+i) == val for i in range(5)) and stone(h-5, w+5) != val and stone(h+1, w-1) != val) \
        or (all(stone(h+i, w+i) == val for i in range(5)) and stone(h+5, w+5) != val and stone(h-1, w-1) != val)

status = 0
xy = None
for j in range(19):
    for i in range(19):
        if stone(i, j) == 0:
            continue
        if check(i, j) and xy is None:
                status = stone(i,j)
                xy = (i, j)

print(status)
if status != 0:
    print(xy[0]+1, xy[1]+1)