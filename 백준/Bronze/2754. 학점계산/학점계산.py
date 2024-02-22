import sys
import re

s = sys.stdin.readline().strip()

dic = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "+": 0.3,
    "0": 0,
    "-": -0.3,
}

if s == "F":
    print("0.0")
else:
    score = dic[s[0]] + dic[s[1]]
    print("{:.1f}".format(score))