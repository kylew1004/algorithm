# https://www.acmicpc.net/problem/16987

import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global ans
    if idx == n:
        ans = max(ans, cnt)
        return
    if eggs[idx][0] <= 0:
        dfs(idx + 1, cnt)
    else:
        flag = False
        for i in range(n):
            if i == idx or eggs[i][0] <= 0:
                continue
            flag = True
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]
            temp = 0
            if eggs[idx][0] <= 0:
                temp += 1
            if eggs[i][0] <= 0:
                temp += 1
            dfs(idx + 1, cnt + temp)
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]
        if not flag:
            dfs(n, cnt)
            
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0, 0)

print(ans)