# https://www.acmicpc.net/problem/1699

# https://www.acmicpc.net/problem/1699

import sys
input = sys.stdin.readline

n = int(input())

dp = [i for i in range(n + 1)]

for i in range(2, int(n ** 0.5) + 1):
    for j in range(i * i, n + 1):
        dp[j] = min(dp[j], dp[j - i * i] + 1)

print(dp[n])
