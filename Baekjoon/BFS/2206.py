# https://www.acmicpc.net/problem/2206

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque([(0, 0, 0)])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    while queue:
        x, y, flag = queue.popleft()
        
        if (x, y) == (n - 1, m - 1):
            return visited[x][y][flag]

        else:
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                        visited[nx][ny][flag] = visited[x][y][flag] + 1
                        queue.append((nx, ny, flag))
                    elif graph[nx][ny] == 1 and flag == 0:
                        visited[nx][ny][1] = visited[x][y][0] + 1
                        queue.append((nx, ny, 1))

    return -1

print(bfs())