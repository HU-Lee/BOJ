import sys

n = int(sys.stdin.readline())
magic_sum = (1 + n**2) * n // 2

magics = []
result = True
for i in range(1, n + 1):
    arr = list(map(int, sys.stdin.readline().split()))
    if sum(arr) != magic_sum:
        result = False
    magics.append(arr)

for i in range(n):
    col_sum = sum(magics[j][i] for j in range(n))
    if col_sum != magic_sum:
        result = False
        break

dia_sum = sum(magics[i][i] for i in range(n))
if dia_sum != magic_sum:
    result = False

dia_sum = sum(magics[i][n - i - 1] for i in range(n))
if dia_sum != magic_sum:
    result = False

number_list = []
for i in range(n):
    number_list.extend(magics[i])
if len(list(set(number_list))) != len(number_list):
    result = False

print("TRUE" if result else "FALSE")

