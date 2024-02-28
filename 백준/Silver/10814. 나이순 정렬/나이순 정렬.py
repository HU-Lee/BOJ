import sys

n = int(sys.stdin.readline().strip())

arr = []
for i in range(n):
    a, n = sys.stdin.readline().strip().split()
    a = int(a)
    arr.append((a,i,n))

arr.sort()

print("\n".join(f'{a} {n}' for a, _, n in arr))