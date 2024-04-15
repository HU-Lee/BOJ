import sys

knights = []
cols = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
}
for _ in range(36):
    pos = sys.stdin.readline().rstrip()
    knights.append((int(pos[1]), cols[pos[0]]))

if not all(
    (abs(knights[i][0] - knights[i - 1][0]) == 1
    and abs(knights[i][1] - knights[i - 1][1]) == 2)
    or (abs(knights[i][0] - knights[i - 1][0]) == 2
    and abs(knights[i][1] - knights[i - 1][1]) == 1)
    for i in range(36)
):
    print("Invalid")
elif len(set(knights)) != 36:
    print("Invalid")
else:
    print("Valid")