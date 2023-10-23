# https://www.acmicpc.net/problem/1182

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

def dfs(idx, sum):
    global result
    if idx >= n:
        return
    sum += arr[idx]
    if sum == s:
        result += 1
    dfs(idx + 1, sum - arr[idx])
    dfs(idx + 1, sum)
    
dfs(0, 0)
print(result)
