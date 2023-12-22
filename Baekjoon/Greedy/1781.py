# https://www.acmicpc.net/problem/1781

import sys, heapq
input = sys.stdin.readline

n = int(input())
problems = [[deadline, cup] for deadline, cup in [list(map(int, input().split())) for _ in range(n)]]
problems.sort()

heap = []
for deadline, cup in problems:
    heapq.heappush(heap, cup)
    if len(heap) > deadline:
        heapq.heappop(heap)
        
print(sum(heap))