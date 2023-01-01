# https://www.acmicpc.net/problem/2468

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0


def dfs(x, y, h):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > h and not visited[nx][ny]:
            dfs(nx, ny, h)


for h in range(101):
    ncnt = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                dfs(i, j, h)
                ncnt += 1
    cnt = max(cnt, ncnt)

print(cnt)
