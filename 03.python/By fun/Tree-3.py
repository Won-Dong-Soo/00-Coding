import sys
input = sys.stdin.readline

def dfs(y, x):
    global cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0 <= nx < m and 0 <= ny < n:
            if cur_map[ny][nx] == '1' and not visited[ny][nx]:
                cnt += 1
                visited[ny][nx] = True
                dfs(ny, nx)
                
def bfs(y, x):
    global cnt
    dq = [(y, x)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while dq:
        y, x = dq.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                if cur_map[ny][nx] == '1' and not visited[ny][nx]:
                    cnt += 1
                    visited[ny][nx] = True
                    dq.append((ny, nx))
        

n, m = map(int, input().strip().split())

cur_map = [['0']*m for _ in range(n)]
for i in range(n):
    cur_map[i] = input().strip().split()
    
visited = [[False]*m for _ in range(n)]\
    
print(cur_map)
print(visited)



cnt = 0
gcnt = []
for i in range(n):
    for j in range(m):
        if cur_map[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            ### DFS
            dfs(i, j)
            
            ###BFS
            # bfs(i, j)
            gcnt.append(cnt)
            cnt = 0
print(gcnt)
            

    

    