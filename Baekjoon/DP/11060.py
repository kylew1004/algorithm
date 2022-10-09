# https://www.acmicpc.net/problem/11060

n = int(input())
arr = list(map(int, input().split()))
dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
    for j in range(arr[i]):
        if i + j + 1 < n:
            dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)
print(dp[n - 1] if dp[n - 1] != float('inf') else -1)
