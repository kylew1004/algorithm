# https://www.acmicpc.net/problem/4485

import sys, heapq
input = sys.stdin.readline

idx = 1

while True:
    n = int(input())

    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    
    heap = []
    heapq.heappush(heap, (graph[0][0], 0, 0))
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    
    while heap:
        cost, x, y = heapq.heappop(heap)
        if x == n-1 and y == n-1:
            answer = cost
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                heapq.heappush(heap, (cost + graph[nx][ny], nx, ny))
                visited[nx][ny] = True
    
    print("Problem {}: {}".format(idx, answer))
    idx += 1