import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

hash_arr = [(ord(l) - ord('a') + 1)*31**i for i, l in enumerate(s)]

print(sum(hash_arr) % 1234567891)