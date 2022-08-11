# https://www.acmicpc.net/problem/11049
# pypy3 로 제출해야함.

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        x = j + i
        dp[j][x] = float('inf')
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + graph[j][0] * graph[k][1] * graph[x][1])
print(dp[0][n - 1])
