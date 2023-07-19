# https://www.acmicpc.net/problem/1965

import sys
input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))