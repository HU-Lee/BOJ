
n = int(input())

map = [list(map(int, input())) for _ in range(n)]

def is_home(x, y, n):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return map[x][y] == 1

def dfs(x, y, n):
    count = 0
    if is_home(x, y, n):
        map[x][y] = 0
        count += 1
        count += dfs(x - 1, y, n)
        count += dfs(x + 1, y, n)
        count += dfs(x, y - 1, n)
        count += dfs(x, y + 1, n)
        return count
    return 0

arr = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            arr.append(dfs(i, j, n))

print(len(arr))
for i in sorted(arr):
    print(i)