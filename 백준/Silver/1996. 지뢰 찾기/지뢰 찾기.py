import sys

n = int(sys.stdin.readline())
arr: list[str] = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())


def get_mine_count(x: int, y: int) -> int:
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    else:
        return int(arr[x][y]) if arr[x][y] != '.' else 0
    
def get_surrounding_mine_count(x: int, y: int) -> int:
    return get_mine_count(x - 1, y - 1) \
        + get_mine_count(x - 1, y) \
        + get_mine_count(x - 1, y + 1) \
        + get_mine_count(x, y - 1) \
        + get_mine_count(x, y + 1) \
        + get_mine_count(x + 1, y - 1) \
        + get_mine_count(x + 1, y) \
        + get_mine_count(x + 1, y + 1)

ans = [[get_surrounding_mine_count(i, j) for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] != '.':
            print('*', end='')
        elif ans[i][j] >= 10:
            print('M', end='')
        else:
            print(ans[i][j], end='')
    print()