# https://www.acmicpc.net/problem/15683

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctv = []

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv.append([arr[i][j], i, j])
            
def check(arr, x, y, d):
    if d == 0:
        for i in range(y, m):
            if arr[x][i] == 6:
                break
            elif arr[x][i] == 0:
                arr[x][i] = '#'
    elif d == 1:
        for i in range(x, n):
            if arr[i][y] == 6:
                break
            elif arr[i][y] == 0:
                arr[i][y] = '#'
    elif d == 2:
        for i in range(y, -1, -1):
            if arr[x][i] == 6:
                break
            elif arr[x][i] == 0:
                arr[x][i] = '#'
    elif d == 3:
        for i in range(x, -1, -1):
            if arr[i][y] == 6:
                break
            elif arr[i][y] == 0:
                arr[i][y] = '#'
                
def dfs(arr, cctv, idx):
    global answer

    if idx == len(cctv):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    cnt += 1
        answer = min(answer, cnt)
        return
    else:
        num, x, y = cctv[idx]
        for i in range(4):
            temp = [row[:] for row in arr]
            if num == 1:
                check(temp, x, y, i)
            elif num == 2:
                check(temp, x, y, i)
                check(temp, x, y, (i + 2) % 4)
            elif num == 3:
                check(temp, x, y, i)
                check(temp, x, y, (i + 1) % 4)
            elif num == 4:
                check(temp, x, y, i)
                check(temp, x, y, (i + 1) % 4)
                check(temp, x, y, (i + 2) % 4)
            elif num == 5:
                check(temp, x, y, i)
                check(temp, x, y, (i + 1) % 4)
                check(temp, x, y, (i + 2) % 4)
                check(temp, x, y, (i + 3) % 4)
            dfs(temp, cctv, idx + 1)
            
answer = 100000
dfs(arr, cctv, 0)
print(answer)
