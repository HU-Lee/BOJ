import sys

arr = []
for i in range(1,9):
    score = int(sys.stdin.readline())
    arr.append((score,i))

arr.sort(reverse=True)

ans = []
sum = 0
for i in range(5):
    sum += arr[i][0]
    ans.append(arr[i][1])

ans.sort()

print(sum)
print(" ".join(map(str,ans)))