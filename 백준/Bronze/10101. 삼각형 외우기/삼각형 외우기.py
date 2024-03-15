import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

if a + b + c != 180:
    print("Error")
else:
    if a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")