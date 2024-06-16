import sys

cnt = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    arr = []
    while True:
        s = sys.stdin.readline().split()
        arr += s
        if len(arr) == n:
            break
    arr = [(val, idx) for idx, val in enumerate(arr)]
    arr = sorted(arr, key=lambda x: x[0])
    print(f'Site {cnt}: {sum(abs(idx - val[1]) for idx, val in enumerate(arr))}')
    cnt += 1