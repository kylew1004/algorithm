# https://www.acmicpc.net/problem/2583

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
            
def dfs(x, y):
    global cnt
    graph[x][y] = 1
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1< nx < m and -1 < ny < n and graph[nx][ny] == 0:
            dfs(nx, ny)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

ans.sort()
print(len(ans))
for i in ans:
    print(i, end=' ')