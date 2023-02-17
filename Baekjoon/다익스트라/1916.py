# https://www.acmicpc.net/problem/1916

import sys
import heapq
input = sys.stdin.readline

def dijkstra():
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, node = heapq.heappop(q)

        if dist[node] < cost:
            continue

        for next_node, next_cost in buses[node]:
            next_cost += cost
            if dist[next_node] > next_cost:
                dist[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))

    return dist


n = int(input())
m = int(input())
buses = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, w = map(int, input().split())
    buses[a].append((b, w))

start, end = map(int, input().split())
dist = dijkstra()

print(dist[end])
