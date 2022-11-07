# https://www.acmicpc.net/problem/11000

import heapq
import sys
input = sys.stdin.readline

n= int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

Q = [0]
for a, b in sorted(arr):
    if Q[0] <= a:
        heapq.heappop(Q)
    heapq.heappush(Q, b)

print(len(Q))
