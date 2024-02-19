import sys
import re

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(sum([1 for i in arr if i == v]))