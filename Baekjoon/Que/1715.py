# https://www.acmicpc.net/problem/1715

import sys, heapq
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)
cnt = 0

while len(cards) > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, tmp)
    cnt += tmp

print(cnt)