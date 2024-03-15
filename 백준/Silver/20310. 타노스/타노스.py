import sys

s = list(map(int, sys.stdin.readline().rstrip()))

one_count = sum(s)

zero_thanos = (len(s)-one_count) //2
one_thanos = 0

ans = ""
for i in s:
    if i == 1:
        if one_thanos < one_count//2:
            one_thanos += 1
        else:
            ans += "1"
    else:
        if zero_thanos > 0:
            zero_thanos -= 1
            ans += "0"    

print(ans)
        


