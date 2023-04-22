# https://www.acmicpc.net/problem/1238

import sys, heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
answer = -1

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])

def dij(start):
    distance = 0
    visited = [float('inf')] * (n+1)
    visited[start] = 0
    heap = [[0, start]]
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        for c, v in graph[node]:
            if visited[v] > cost + c:
                visited[v] = cost + c
                heapq.heappush(heap, [cost + c, v])

    distance += visited[x]
    visited = [float('inf')] * (n+1)
    visited[x] = 0
    heap = [[0, x]]
    
    while heap:
        cost, node = heapq.heappop(heap)

        for c, v in graph[node]:
            if visited[v] > cost + c:
                visited[v] = cost + c
                heapq.heappush(heap, [cost + c, v])

    distance += visited[start]

    return distance


for i in range(1, n+1):
    if i != x:
        answer = max(answer, dij(i))

print(answer)