# https://www.acmicpc.net/problem/9663

import sys
input = sys.stdin.readline

n = int(input())
graph = [0] * n
res = 0

def check(x):
    for i in range(x):
        if graph[x] == graph[i] or abs(x - i) == abs(graph[x] - graph[i]):
            return False
    return True

def dfs(x):
    global res

    if x == n:
        res += 1
        return
    
    for i in range(n):
        graph[x] = i
        if check(x):
            dfs(x + 1)

dfs(0)
print(res)