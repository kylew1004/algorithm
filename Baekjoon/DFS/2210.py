# https://www.acmicpc.net/problem/2210

import sys
input = sys.stdin.readline

def dfs(x, y, n):
    n += graph[x][y]
    
    if len(n) == 6:
        if n not in visited:
            visited.append(n)
        return
    
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i, j in moves:
        dx = x + i
        dy = y + j
        if dx >= 5 or dy >= 5 or dx < 0 or dy < 0:
            continue
        else:
            dfs(dx, dy, n)
    
graph = []
visited = []
for i in range(5):
    graph.append(list(map(str, input().split())))

for i in range(5):
    for j in range(5):
        dfs(i, j, "")
print(len(visited))