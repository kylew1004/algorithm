# https://www.acmicpc.net/problem/1003

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = int(input())
    dp = [[0, 0] for _ in range(t + 1)]
    dp[0] = [1, 0]
    if t > 0:
        dp[1] = [0, 1]
        for i in range(2, t + 1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]
    print(dp[t][0], dp[t][1])