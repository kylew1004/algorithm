# https://www.acmicpc.net/problem/2211

import sys, heapq
input = sys.stdin.readline

n, m = map(int,(input().split()))
node = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    node[a].append([b, c])
    node[b].append([a, c])
    
heap = [(0, 1)]
D = [float('inf')] * (n + 1)
D[1] = 0
parent = [0] * (n + 1)

while heap:
    SD, SN = heapq.heappop(heap)
    
    if D[SN] < SD:
        continue

    for FN, FD in node[SN]:
        d = SD + FD
        if D[FN] > d:
            D[FN] = d
            parent[FN] = SN
            heapq.heappush(heap, (d, FN))

print(n - 1)
for i in range(2, n + 1):
    print(i, parent[i])