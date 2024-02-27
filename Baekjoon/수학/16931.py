# https://www.acmicpc.net/problem/16931

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 2 * n * m

for i in range(n):
    for j in range(m):
        if i == 0:
            ans += arr[i][j]
        else:
            ans += abs(arr[i][j] - arr[i - 1][j])
        if j == 0:
            ans += arr[i][j]
        else:
            ans += abs(arr[i][j] - arr[i][j - 1])
        if i == n - 1:
            ans += arr[i][j]
        if j == m - 1:
            ans += arr[i][j]

print(ans)