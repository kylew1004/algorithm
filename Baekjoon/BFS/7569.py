# https://www.acmicpc.net/problem/7569

from collections import deque

m, n, h = map(int,input().split())
a = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if a[nz][nx][ny] == 0:
                    a[nz][nx][ny] = a[z][x][y] + 1
                    queue.append([nz, nx, ny])

queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k] == 1:
                queue.append([i, j, k])

bfs()

z = 1
result = -1

for i in a:
    for j in i:
        for k in j:
            if k == 0:
                z = 0
            result = max(result, k)

if z == 0:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)