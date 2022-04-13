# https://www.acmicpc.net/problem/13460

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "R":
            rx, ry = i, j
        elif graph[i][j] == "B":
            bx, by = i, j

def check(x, y, dx, dy):
    while True:
        x += dx
        y += dy
        if graph[x][y] == "#":
            x -= dx
            y -= dy
            return x, y
        if graph[x][y] == "O":
            return x, y

def bfs(rx, ry, bx, by):
    queue = deque()
    visited = []
    count = 0
    visited.append((rx, ry, bx, by))
    queue.append((rx, ry, bx, by))
    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()
            if count > 10:
                print(-1)
                return
            if graph[rx][ry] == "O":
                print(count)
                return
            for i in range(4):
                nrx, nry = check(rx, ry, dx[i], dy[i])
                nbx, nby = check(bx, by, dx[i], dy[i])
                if graph[nbx][nby] == "O":
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx- bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1)

bfs(rx, ry, bx, by)        