import sys

n,k = map(int,sys.stdin.readline().split())
arr = sorted(list(map(int,sys.stdin.readline().split())), reverse=True)

print(sum(arr[:k]) - k*(k-1)//2)