# https://www.acmicpc.net/problem/16395

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[1] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n):
    dp[i][0] = 1
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        
print(dp[n - 1][k - 1])