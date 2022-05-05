# https://www.acmicpc.net/problem/11779

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
start, end = map(int, (input().split()))

def dijkstra(start, distance, graph):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    visited[start] = [start]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if distance[x[0]] > cost:
                heapq.heappush(q, [cost, x[0]])
                distance[x[0]] = cost
                visited[x[0]] = visited[now] + [x[0]]

dijkstra(start, distance, graph)
print(distance[end])
print(len(visited[end]))
print(" ".join(map(str, visited[end])))