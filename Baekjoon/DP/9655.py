# https://www.acmicpc.net/problem/9655

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001

dp[1] = 0
dp[2] = 1
dp[3] = 0

for i in range(4, n+1):
    if dp[i-1] == 0 or dp[i-3] == 0:
        dp[i] = 1

print("SK" if dp[n] == 0 else "CY")