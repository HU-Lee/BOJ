import sys
import collections

s = sys.stdin.readline().strip()

dic = collections.defaultdict(int)
for i in s.upper():
    dic[i] += 1

m = max(dic.values())

letters = [x for x in dic if dic[x] == m]
if len(letters) > 1:
    print("?")
else:
    print(letters[0])