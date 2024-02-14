import sys
import math

n = int(sys.stdin.readline())

arr = sorted(list(map(int, sys.stdin.readline().split(" "))))
total_score = sum(arr)/max(arr)*100
print(total_score/n)