# https://www.acmicpc.net/problem/11047

import sys 
input = sys.stdin.readline

N, K = map(int,input().split())
arr = [int(input()) for _ in range(N)]
cnt, idx = 0, N-1

while K > 0:
    if arr[idx] > K:
        idx -= 1
    else:
        cnt += K//arr[idx]
        K %= arr[idx]
print(cnt)