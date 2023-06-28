# https://www.acmicpc.net/problem/13305

import sys
input = sys.stdin.readline

k = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
min_cost = 0

min_pos = cost[0]
for i in range(k - 1):
    if min_pos > cost[i]:
        min_pos = cost[i]
    min_cost += min_pos * dist[i]

print(min_cost)