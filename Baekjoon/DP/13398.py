# https://www.acmicpc.net/problem/13398

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0, 0] for _ in range(n)]
dp[0] = [nums[0], nums[0]]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + nums[i], nums[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + nums[i])

print(max(map(max, dp)))