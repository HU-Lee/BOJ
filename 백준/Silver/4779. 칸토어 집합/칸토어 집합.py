import sys

def solution(n):
    if n == 0:
        return "-"
    else:
        return solution(n-1) + " "*(3**(n-1)) + solution(n-1)

while True:
    try:
        n = int(sys.stdin.readline())
        print(solution(n))
    except:
        break