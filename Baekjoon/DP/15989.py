# https://www.acmicpc.net/problem/15989

t = int(input())
cases = [int(input()) for _ in range(t)]
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for i in range(t):
    print(dp[cases[i]])
