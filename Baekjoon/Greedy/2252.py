# https://www.acmicpc.net/problem/2252

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
lst = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    lst[b] += 1

queue = deque()

for i in range(1, n + 1):
    if lst[i] == 0:
        queue.append(i)

answer = []

while queue :
    now = queue.popleft()
    answer.append(now)
    for i in graph[now]:
        lst[i] -= 1
        if lst[i] == 0 :
            queue.append(i)

for a in answer:
    print(a, end=' ')