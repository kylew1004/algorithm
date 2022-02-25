# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

def dfs(graph, visited, V):
    visited[V] = True
    print(V, end = " ")
    
    for i in graph[V]:
        if not visited[i]:
            dfs(graph, visited, i)
    
def bfs(graph, visited, V):
    queue = deque([V])
    visited[V] = True
    while queue:
        pop = queue.popleft()
        print(pop, end = " ")

        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a ,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()
    
dfs(graph, [False] * (N + 1), V)
print()
bfs(graph, [False] * (N + 1), V)