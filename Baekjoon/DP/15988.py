# https://www.acmicpc.net/problem/15988

t = int(input())
dp = [0 for _ in range(1000001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

num = []
for _ in range(t):
    num.append(int(input()))

for n in num:
    print(dp[n] % 1000000009)