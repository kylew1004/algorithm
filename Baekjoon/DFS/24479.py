# https://www.acmicpc.net/problem/24479

import sys, heapq
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
visited = [0] * n
graph = [[] for _ in range(n)]
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    heapq.heappush(graph[a - 1], b - 1)
    heapq.heappush(graph[b - 1], a - 1)

def dfs(v):
    global cnt
    visited[v] = cnt
    
    while graph[v]:
        w = heapq.heappop(graph[v])
        if not visited[w]:
            cnt += 1
            dfs(w)

dfs(r - 1)

for i in range(n):
    print(visited[i])