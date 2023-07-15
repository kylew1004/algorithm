# https://www.acmicpc.net/problem/9372

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    cnt = 0
    
    while q:
        q.popleft()
        for nx in range(1, n + 1):
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
                cnt += 1
    return cnt


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for i in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    print(bfs(1))


'''
# 뭐야 이거
for _ in range(int(input())):
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
    print(n - 1)
'''