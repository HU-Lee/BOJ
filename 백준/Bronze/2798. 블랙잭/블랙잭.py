import sys

a,b = map(int,sys.stdin.readline().split())
arr = sorted(list(map(int,sys.stdin.readline().split())))

max_val = 0
for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            sum = arr[i] + arr[j] + arr[k]
            if sum > b: break
            elif sum > max_val:
                max_val = sum

print(max_val)