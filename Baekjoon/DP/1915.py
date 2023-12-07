# https://www.acmicpc.net/problem/1915

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            answer = max(answer, dp[i][j])

print(answer ** 2)