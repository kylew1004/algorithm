# https://www.acmicpc.net/problem/1904

n = int(input())
dp = [0] * (n + 2)  # n 이 1일때를 대비해 n + 2

dp[1] , dp[2] = 1, 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])