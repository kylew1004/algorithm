# https://www.acmicpc.net/problem/7795

import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    result = 0
    cnt = 0
    
    for i in range(n):
        while True:
            if cnt == m or a[i] <= b[cnt]:
                result += cnt
                break
            else:
                cnt += 1

    print(result)