# https://www.acmicpc.net/problem/2098

import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (1 << n) for _ in range(n)]

def tsp(here, visited):
    if visited == (1 << n) - 1:
        return w[here][0] if w[here][0] > 0 else float('inf')
    if dp[here][visited] != -1:
        return dp[here][visited]
    dp[here][visited] = float('inf')
    for i in range(n):
        if visited & (1 << i) == 0 and w[here][i] > 0:
            dp[here][visited] = min(dp[here][visited], tsp(i, visited | (1 << i)) + w[here][i])
    return dp[here][visited]

print(tsp(0, 1))