# https://www.acmicpc.net/problem/12026

n = int(input())
arr = list(input())

dp = [float('inf')] * n
dp[0] = 0

def ex(x):
    if x == "B":
        return "J"
    elif x == "O":
        return "B"
    elif x == "J":
        return "O"

for i in range(1, n):
    prev = ex(arr[i])
    for j in range(i):
        if arr[j] == prev:
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))

print(dp[n - 1] if dp[n - 1] != float('inf') else -1)