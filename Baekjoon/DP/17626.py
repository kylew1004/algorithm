# https://www.acmicpc.net/problem/17626

import sys
input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n + 1)]
squares = [i * i for i in range(1, int(n**0.5) + 1)]

for i in range(1, n + 1):
    for square in squares:
        if square > i:
            break
        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[n])
