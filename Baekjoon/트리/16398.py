# https://www.acmicpc.net/problem/16398

import sys
import heapq
input = sys.stdin.readline

n = int(input())
costs = []
p = [i for i in range(n)]
q = []

for _ in range(n):
    costs.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i+1, n):
        heapq.heappush(q, (costs[i][j], i, j))


def find(a):
    if p[a] == a:
        return a

    p[a] = find(p[a])
    return p[a]


def union(a, b):
    a = find(a)
    b = find(b)

    p[a] = b


answer, cnt = 0, 0
while cnt != n - 1:
    cost, a, b = heapq.heappop(q)

    if find(a) != find(b):
        union(a, b)
        answer += cost
        cnt += 1

print(answer)