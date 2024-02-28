import sys
sys.setrecursionlimit(10**6)


dic = {
    0: 0,
    1: 1,
    2: 1
}
def fibo(n):
    if n <= 2:
        return dic[n]
    else:
        if n not in dic:
            if n % 2 == 0:
                k = n//2
                dic[n] = (fibo(k-1)*2 + fibo(k))*fibo(k)%1000000007
            else:
                k = (n+1)//2
                dic[n] = (fibo(k)*fibo(k) + fibo(k-1)*fibo(k-1))%1000000007
    return dic[n]

i = int(sys.stdin.readline().strip())

print(fibo(i))