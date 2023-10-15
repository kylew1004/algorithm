# https://www.acmicpc.net/problem/1100

import sys
input = sys.stdin.readline

chess = [list(input().rstrip()) for _ in range(8)]
cnt = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and chess[i][j] == 'F':
            cnt += 1
            
print(cnt)
