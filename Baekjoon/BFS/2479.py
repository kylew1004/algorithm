# https://www.acmicpc.net/problem/2479

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, last):
    queue = deque()
    queue.append((start, [start]))

    while queue:
        q, path = queue.popleft()
        if q == last:
            return ' '.join(map(str, path))
        for i in range(1, n+1):
            if not visited[i]:
                cnt = 0
                for j in range(k):
                    if arr[q][j] != arr[i][j]:
                        cnt += 1
                        if cnt > 1:
                            break
                if cnt == 1:
                    queue.append((i, path + [i]))
                    visited[i] = 1
    return -1

n, k = map(int, input().split())
arr = [0] + [input() for _ in range(n)]
visited = [0] * (n+1)
start, last = map(int, input().split())
print(bfs(start, last))