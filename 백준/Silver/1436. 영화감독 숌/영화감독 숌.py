import sys

arr = [i for i in range(666, 6666666) if "666" in str(i)]

n = int(sys.stdin.readline())
print(arr[n-1])
        