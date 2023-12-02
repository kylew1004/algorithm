# https://atcoder.jp/contests/abc331/tasks/abc331_b

import sys
input = sys.stdin.readline

n, s, m, l = map(int, input().split())
dp = [-1] * (n + 12)
answer = float('inf')

for i in range(1, n + 12):
    dp[i] = float('inf')

    if i >= 6:
        dp[i] = min(dp[i], s + dp[i - 6])
    if i >= 8:
        dp[i] = min(dp[i], m + dp[i - 8])
    if i >= 12:
        dp[i] = min(dp[i], l + dp[i - 12])

for i in range(n, n + 12):
    if dp[i] != float('inf') and dp[i] != -1:
        answer = min(answer, dp[i] + 1)

print(answer)