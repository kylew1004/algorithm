# https://www.acmicpc.net/problem/9251
# dp를 1차원으로 풀려다 결국 못품;

x = ' ' + input()
y = ' ' + input()

dp = [[0] * (len(y)) for _ in range(len(x))]

for i in range(1, len(x)):
    for j in range(1, len(y)):
        if x[i] == y[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
