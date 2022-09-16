# https://www.acmicpc.net/problem/16948

from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
graph = [[-1] * n for _ in range(n)]
moves = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

queue = deque()
queue.append([r1, c1])
graph[r1][c1] = 0

while queue:
    r, c = queue.popleft()
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if (0 <= nr < n) and (0 <= nc < n) and graph[nr][nc] == -1:
            queue.append([nr, nc])
            graph[nr][nc] = graph[r][c] + 1

print(graph[r2][c2])