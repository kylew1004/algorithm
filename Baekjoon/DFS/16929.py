# https://www.acmicpc.net/problem/16929

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
flag = 0

def scope(y, x):
    if y >= 0 and y < n and x >= 0 and x < m:
        return True
    else:
        return False

def dfs(y, x, py, px, ball):
    if visited[y][x] == 1:
        return True

    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny != py or nx != px:
            if scope(ny,nx) and graph[ny][nx] == ball:
                if dfs(ny, nx, y, x, ball):
                    return True
    return False

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        if dfs(i, j, 0, 0, graph[i][j]):
            flag = True
            break

print("Yes") if flag else print("No")