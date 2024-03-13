import sys
import math

# n*(n-1)/2 < k <= n*(n+1)/2
# (n-0.5)**2 < 2*k+0.25 <= (n+0.5)**2
# n-1 < math.sqrt(2 * k + 0.25)-0.5 <= n

k = int(sys.stdin.readline())

n = math.ceil(math.sqrt(2 * k + 0.25)-0.5)

x = n*(n+1)//2 - k

if n % 2 == 0:
    print(f'{n-x}/{x+1}')
else:
    print(f'{x+1}/{n-x}')