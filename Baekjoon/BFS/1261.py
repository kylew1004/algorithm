# https://www.acmicpc.net/problem/1261

from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dp = [[-1] * m for _ in range(n)]
dp[0][0] = 0
queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if dp[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    dp[nx][ny] = dp[x][y]
                    queue.appendleft((nx, ny))
                else:
                    dp[nx][ny] = dp[x][y] + 1
                    queue.append((nx, ny))

print(dp[n - 1][m - 1])