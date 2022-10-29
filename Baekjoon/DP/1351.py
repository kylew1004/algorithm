# https://www.acmicpc.net/problem/1351

n, p, q = map(int, input().split())
dp = {0 : 1}

def dfs(n):
    if n in dp:
        return dp[n]
    else:
        dp[n] = dfs(n // p) + dfs(n // q)
        return dp[n]

print(dfs(n))
