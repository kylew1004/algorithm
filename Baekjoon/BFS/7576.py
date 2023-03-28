# https://www.acmicpc.net/problem/7576

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j, cnt))

while queue:
    x, y, cnt = queue.popleft()

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
            if graph[nx][ny] == 0:
                queue.append((nx, ny, cnt + 1))
                graph[nx][ny] = 1

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt = -1

print(cnt)