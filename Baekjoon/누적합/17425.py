# https://www.acmicpc.net/problem/17425
# pypy3 로 제출해야 시간초과가 안난다.

import sys
input = sys.stdin.readline

dp = [0] * 1000001

for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        dp[j] += i
    dp[i] += dp[i - 1]

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])