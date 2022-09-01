# https://www.acmicpc.net/problem/13023

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n
check = False

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start, depth):
    global check
    visited[start] = True

    if depth == 4:
        check = True
        return
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)
            visited[i] = False

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if check:
        break

print(1 if check else 0)