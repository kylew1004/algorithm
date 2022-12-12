# https://www.acmicpc.net/problem/1138

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    for j in range(n):
        if arr[i] == 0 and dp[j] == 0:
            dp[j] = i + 1
            break
        elif dp[j] == 0:
            arr[i] -= 1
            
print(' '.join(map(str, dp)))
