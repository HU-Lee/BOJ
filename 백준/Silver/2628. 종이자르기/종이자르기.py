import sys

a,b = map(int,sys.stdin.readline().split())

widths = [0, a]
heights = [0, b]

n = int(sys.stdin.readline())

for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    if x == 1:
        widths.append(y)
    else:
        heights.append(y)

widths.sort()
heights.sort()

mw = max([widths[i+1]-widths[i] for i in range(len(widths)-1)])
mh = max([heights[i+1]-heights[i] for i in range(len(heights)-1)])
print(mw*mh)
