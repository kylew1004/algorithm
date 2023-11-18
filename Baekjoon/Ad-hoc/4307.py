# https://www.acmicpc.net/problem/4307

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    l, n = map(int, input().split())
    ants = [int(input()) for _ in range(n)]
    min_time = 0
    max_time = 0
    for ant in ants:
        min_time = max(min_time, min(ant, l-ant))
        max_time = max(max_time, max(ant, l-ant))

    print(min_time, max_time)