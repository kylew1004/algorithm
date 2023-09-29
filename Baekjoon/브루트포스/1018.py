# https://www.acmicpc.net/problem/1018

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
ans = 64

for i in range(n - 7):
    for j in range(m - 7):
        cnt = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        cnt += 1
                else:
                    if board[k][l] != 'B':
                        cnt += 1
        ans = min(ans, cnt, 64 - cnt)
        
print(ans)
