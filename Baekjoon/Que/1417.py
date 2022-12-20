# https://www.acmicpc.net/problem/1417

import heapq

n = int(input())
dasom = int(input())
q = []
for _ in range(n - 1):
    vote = int(input())
    heapq.heappush(q, -vote)
    
answer = 0

while q:
    vote = -heapq.heappop(q)
    if dasom > vote:
        break
    dasom += 1
    answer += 1
    heapq.heappush(q, -(vote - 1))

print(answer)
