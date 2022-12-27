# https://www.acmicpc.net/problem/1309

import sys
input = sys.stdin.readline

n = int(input())
dp = [[1, 1, 1] for _ in range(n + 1)]

for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][1] + dp[i - 1][0] + dp[i - 1][2]) % 9901

print(sum(dp[n]) % 9901)
