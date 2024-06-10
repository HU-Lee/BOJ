import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

result = arr[-1]
for i in arr[:-1][::-1]:
    if i == "LIE":
        result = "LIE" if result == "TRUTH" else "TRUTH"

print(result)