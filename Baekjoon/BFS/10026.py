# https://www.acmicpc.net/problem/10026

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    queue = deque()
    queue.append([a, b])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1


n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
visited = [[0] * n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)