# https://www.acmicpc.net/problem/24542

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
nodes = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int,input().split())
    nodes[x].append(y)
    nodes[y].append(x)
visited = [0] * (n + 1)
visited_cnt = 1
cnt = []

for i in range(1, n + 1):
    queue = deque()
    queue.append(i)
    if not visited[i]: 
        visited[i] = 1
        cnt.append(1)
        while queue:
            q = queue.popleft()

            for i in nodes[q]:
                if not visited[i]:
                    queue.append(i)
            if not visited[q]:
                visited[q] = 1
                visited_cnt += 1
                cnt[-1] += 1

answer = 1
for c in cnt:
    answer *= c
print(answer % 1000000007)