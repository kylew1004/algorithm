# https://www.acmicpc.net/problem/2644

from collections import deque

n = int(input())
n1, n2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
count = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)

queue = deque()
queue.append(n1)
while queue:
    q = queue.popleft()

    for i in graph[q]:
        if count[i] == 0:
            count[i] = count[q] + 1
            queue.append(i)

print(count[n2] if count[n2] > 0 else -1)