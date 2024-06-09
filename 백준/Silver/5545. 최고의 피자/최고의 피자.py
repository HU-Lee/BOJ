import sys

c = int(sys.stdin.readline().rstrip())
dow_p, top_p = map(int, sys.stdin.readline().rstrip().split())
dow_cal = int(sys.stdin.readline().rstrip())

top_cals = []
for _ in range(c):
    top_cals.append(int(sys.stdin.readline().rstrip()))

top_cals.sort(reverse=True)

cal = dow_cal
price = dow_p
for top_cal in top_cals:
    if (cal + top_cal) / (price + top_p) >= cal / price:
        cal += top_cal
        price += top_p
    else:
        break

print(cal // price)