import sys

dic = {
    1:1,
    2:1
}

n = int(sys.stdin.readline())

def fibo(x):
    if x in dic:
        return dic[x]
    else:
        dic[x] = fibo(x-1) + fibo(x-2)
        return dic[x]
    
print(fibo(n), n-2)