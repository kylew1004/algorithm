# https://www.acmicpc.net/problem/13913

import sys
from collections import deque
input = sys.stdin.readline
MAX = 10 ** 5

def bfs(n,k,dp):
    queue = deque()
    visited = [0] * (MAX + 1)
    path = []
    queue.append(n)
    while queue:
        q = queue.popleft()
        if q == k:
            print(dp[k])
            while q != n:
                path.append(q)
                q = visited[q]
            path.append(n)
            path.reverse()
            print(' '.join(map(str, path)))
            return
        for i in (q-1, q+1, 2*q):
            if 0 <= i <= MAX and dp[i] == 0:
                dp[i] = dp[q] + 1
                queue.append(i)
                visited[i] = q

n, k = map(int, input().split())
dp = [0] * (MAX + 1)
bfs(n, k, dp)