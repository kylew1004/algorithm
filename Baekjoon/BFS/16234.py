# https://www.acmicpc.net/problem/16234

from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

days = 0

def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    toChange = [(i, j)]
    total = graph[i][j]
    flag = False

    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    toChange.append((nx, ny))
                    total += graph[nx][ny]
                    flag = True

    return toChange, total, flag


while True:
    visited = [[False] * n for _ in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                toChange, total, flag = bfs(i, j)

                if flag:
                    isTrue = True
                    avg = total // len(toChange)
                    for x, y in toChange:
                        graph[x][y] = avg

    if not isTrue:
        break

    days += 1

print(days)