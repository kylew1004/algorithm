# https://www.acmicpc.net/problem/14501

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + graph[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(graph[i][1] + dp[i + graph[i][0]], dp[i+1])

print(dp[0])