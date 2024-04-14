# https://www.acmicpc.net/problem/2566

import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
max_val = max(map(max, arr))
x, y = 0, 0

for i in range(9):
    for j in range(9):
        if arr[i][j] == max_val:
            x, y = i, j
            break
        
print(max_val)
print(x + 1, y + 1)
