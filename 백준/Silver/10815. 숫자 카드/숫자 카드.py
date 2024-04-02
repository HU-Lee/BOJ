import sys

n = int(sys.stdin.readline())
deck = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ans = list(map(lambda x: 1 if x in deck else 0, arr))
print(" ".join(map(str, ans)))