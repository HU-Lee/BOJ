import sys

r,c = map(int,sys.stdin.readline().split())

cayac = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

result = [-1 for _ in range(9)]
for arr in cayac:
    x = arr[::-1]
    for idx, s in enumerate(x):
        if s not in ["S", "F", "."]:
            result[int(s)-1] = idx

rank = sorted(list(set(result)))

result = [rank.index(i) + 1 for i in result]

print("\n".join(map(str,result)))