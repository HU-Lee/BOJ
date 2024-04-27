import sys

a,b = sys.stdin.readline().split()

k = len(b) - len(a)
ans = len(b)
for i in range(k+1):
    new_a = '0'*i + a + '0'*(k-i)
    diff = [1 for i in range(len(b)) if b[i] != new_a[i] and new_a[i] != '0']
    ans = min(ans, len(diff))

print(ans)