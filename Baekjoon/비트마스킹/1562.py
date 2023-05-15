# https://www.acmicpc.net/problem/1562
# 진짜 ㅈㄴ 어렵다 쉬워보여서 끄적이다 문제를 잘못 선정했다는 것을 깨달았다.

import sys
input = sys.stdin.readline

n = int(input())
answer = 0

dp = [[[0 for _ in range(10)] for _ in range(1024)] for _ in range(n+1)]    # dp[i][j][k] : i자리수, j는 0~9까지의 숫자를 모두 포함하는지 여부, k는 마지막 숫자

for i in range(1, 10):
    dp[1][1 << i][i] = 1    # 1자리수일때 1~9까지의 숫자를 모두 포함하는 경우의 수는 1

for i in range(2, n+1):
    for j in range(1024):
        for k in range(10):
            if k == 0:  # 0일때는 1밖에 못오니까
                dp[i][j | (1 << k)][k] += dp[i-1][j][1]
            elif k == 9:    # 9일때는 8밖에 못오니까
                dp[i][j | (1 << k)][k] += dp[i-1][j][8]
            else:   # 0~8까지는 양쪽으로 올 수 있음
                dp[i][j | (1 << k)][k] += dp[i-1][j][k-1] + dp[i-1][j][k+1]

for i in range(10):
    answer += dp[n][1023][i]

print(answer % 1000000000)