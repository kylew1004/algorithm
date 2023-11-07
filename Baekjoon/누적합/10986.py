# https://www.acmicpc.net/problem/10986

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
cnt = [0] * m
answer = 0

for i in range(1, n + 1):
    dp[i] = (dp[i - 1] + arr[i - 1]) % m

for i in range(n + 1):
    cnt[dp[i]] += 1

for i in range(m):
    answer += cnt[i] * (cnt[i] - 1) // 2

print(answer)