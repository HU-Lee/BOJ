import sys

n = int(sys.stdin.readline())
sum = 0
arr_str = sys.stdin.readline().rstrip() 

tmp = ""
for i in arr_str:
    if not i.isdigit():
        sum += int(tmp)
        tmp = ""
    else:
        tmp += i
sum += int(tmp)

print(sum - n*(n-1)//2)