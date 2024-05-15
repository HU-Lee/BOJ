import sys

n,m = map(int,sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

# 외부 공간 체크
exts = [[False]*m for _ in range(n)]

def updateExt():
    for x in range(n):
        for y in range(m):
            exts[x][y] = False
    exts[0][0] = True
    q = [(0,0)]
    while q:
        x,y = q.pop(0)
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not exts[nx][ny] and arr[nx][ny] == 0:
                exts[nx][ny] = True
                q.append((nx,ny))

def surroundings(x,y):
    ans = 0
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if exts[nx][ny]:
            ans += 1
    return ans

def dfs(cnt):
    if sum(sum(arr[x]) for x in range(n)) == 0:
        print(cnt)
        return

    updateExt()

    newArr = [[arr[x][y] for y in range(m)] for x in range(n)]
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1 and surroundings(x,y) >= 2:
                newArr[x][y] = 0
    for x in range(n):
        for y in range(m):
            arr[x][y] = newArr[x][y]
    dfs(cnt+1)

dfs(0)