import sys

def check(word):
    arr = []
    tmp = "X"
    for _, s in enumerate(word):
        if s != tmp:
            tmp = s
            arr.append(s)
    return len(arr) == len(set(arr))


n = int(sys.stdin.readline().strip())
cnt = 0
for _ in range(n):
    word = sys.stdin.readline().strip()
    if check(word):
        cnt += 1

print(cnt)