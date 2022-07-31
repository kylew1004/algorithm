# https://www.acmicpc.net/problem/2667

from collections import deque

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
counts = []

def bfs(x, y):
  dx = [-1, 1, 0, 0]  
  dy = [0, 0, -1, 1]
  queue = deque()
  queue.append((x, y))
  graph[x][y] = 0
  count = 1

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
        count += 1
  counts.append(count)

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      bfs(i, j)

counts.sort()
print(len(counts))

for i in counts:
  print(i)