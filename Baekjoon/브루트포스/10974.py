# https://www.acmicpc.net/problem/10974

import sys
input = sys.stdin.readline

n = int(input())
arr = [i for i in range(1, n + 1)]
result = []

def dfs():
    if len(result) == n:
        print(*result)
        return
    for i in range(n):
        if arr[i] not in result:
            result.append(arr[i])
            dfs()
            result.pop()
            
dfs()
