# https://www.acmicpc.net/problem/16947

import sys
from collections import deque
sys.setrecursionlimit(10**5)

n = int(input())
station = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
for i, j in station:
    graph[i - 1].append(j - 1)
    graph[j - 1].append(i - 1)
cycle = []
answer = [0] * n


def find_cycle(path, visited):
    global cycle

    if path[0] == path[-1] and len(path) > 3:
        cycle = path[:-1]
    elif not visited[path[-1]]:
        visited[path[-1]] = 1
        for i in graph[path[-1]]:
            path.append(i)
            find_cycle(path, visited)
            path.pop()


def count_distance(node, cycle, answer):
    queue = deque([[node, 0]])
    visited = [0] * n

    while queue:
        q, cnt = queue.popleft()
        answer[q] = cnt
        visited[q] = 1
        for i in graph[q]:
            if not visited[i] and i not in cycle:
                queue.append([i, cnt + 1])
    return answer


for i in range(n):
    if not cycle:
        find_cycle([i], [0] * n)
    else:
        break

for node in cycle:
    answer = count_distance(node, cycle, answer)

print(" ".join(map(str, answer)))
