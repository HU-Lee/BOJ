import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

lever = 1
position = 0
kill = 0
for command in s:
    if command == 'P':
        if lever != -1:
            lever = (lever + 1) % 2
        if position == 1:
            lever = -1
    else:
        position += 1
        if position == 2:
            if lever == 1:
                kill = 5
            elif lever == 0:
                kill = 1
            else:
                kill = 6
            break

print(kill)