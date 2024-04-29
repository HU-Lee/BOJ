import sys

arr = list(map(int, sys.stdin.readline().split()))

state = ""
if arr[0] == 1:
    state = "ascending"
elif arr[0] == 8:
    state = "descending"
else:
    state = "mixed"
for i in range(1, 8):
    if state == "mixed":
        break
    if arr[i] == arr[i - 1] + 1 and state == "ascending":
        continue
    elif arr[i] == arr[i - 1] - 1 and state == "descending":
        continue
    else:
        state = "mixed"
    
print(state)