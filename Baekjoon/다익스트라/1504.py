# https://www.acmicpc.net/problem/1504

import sys, heapq
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((cost, y))
    graph[y].append((cost, x))


def dij(start, end):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [[0, start]]

    while heap:
        cost, node = heapq.heappop(heap)

        if cost <= dist[node]:
            for c, v in graph[node]:
                if dist[v] > dist[node] + c:
                    dist[v] = dist[node] + c
                    heapq.heappush(heap, [dist[v], v])

    return dist[end]


v1, v2 = map(int, input().split())
path1 = dij(1, v1) + dij(v1, v2) + dij(v2, n)
path2 = dij(1, v2) + dij(v2, v1) + dij(v1, n)

print(min(path1, path2) if max(path1, path2) < float('inf') else -1)