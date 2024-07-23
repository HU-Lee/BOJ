import sys

arr = ['000', '001', '010', '011', '100', '101', '110', '111']

n = sys.stdin.readline().rstrip()

if n == '0':
    print(0)
else:
    li = []

    for i in range(len(n)):
        li.append(arr[int(n[i])])

    ans = ''.join(li)

    while ans[0] == '0':
        ans = ans[1:]

    print(ans)