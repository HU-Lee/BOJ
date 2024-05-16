import sys

r,c = map(int,sys.stdin.readline().split())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

visited = [False]*26

ans = 0

def dfs(x,y,val):
    global ans
    ans = max(ans,val)
    if ans == 26:
        return

    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
        nx,ny = x+dx,y+dy
        if 0<=nx<r and 0<=ny<c:
            idx = ord(arr[nx][ny])-ord('A')    
            if not visited[idx]:
                visited[idx] = True
                dfs(nx,ny,val+1)
                visited[idx] = False

visited[ord(arr[0][0])-ord('A')] = True
dfs(0,0,1)
print(ans)