# https://www.acmicpc.net/problem/2056

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    works = list(map(int, input().split()))

    for num in works[1:]:
        dp[i] = max(dp[i], dp[num] + works[0])

print(max(dp))