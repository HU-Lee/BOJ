import sys

while True:
    try:
        s = sys.stdin.readline().strip()
        if len(s) > 0:
            print(s)
        else:
            break
    except:
        sys.exit()