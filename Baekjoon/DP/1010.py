# https://www.acmicpc.net/problem/1010

t = int(input())
dp = [[0] * 30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

for _ in range(t):
    n, m = list(map(int, input().split()))
    print (dp[n][m])