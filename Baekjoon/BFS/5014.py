# https://www.acmicpc.net/problem/5014

import sys
from collections import deque

def bfs():
    visited = [1e9] * 1000001
    queue = deque([s])
    visited[s] = 0
    while queue:
        target = queue.popleft()

        if target == g:
            return visited[target]

        for i in (u, -d):
            if 1 <= i + target <= f and visited[i + target] == 1e9:
                visited[i + target] = min(visited[target] + 1, visited[i + target])
                queue.append(i + target)

    return "use the stairs"


f, s, g, u, d = map(int, sys.stdin.readline().split())

print(bfs())