import sys

# 짝수면 후자, 홀수면 전자가 이기는 것 같습니다만??
n = int(sys.stdin.readline())

print("SK" if n % 2 else "CY")