# https://www.acmicpc.net/problem/1647
# import sys 는 잘 안하는데 안하게 되면 시간초과가 뜬다. 오랜만에 썼다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
parents = [i for i in range(n + 1)]
answer = 0
max_cost = 0

graph.sort(key=lambda x: x[2])


def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]


def union(start, end):
    start = find(start)
    end = find(end)

    if start < end:
        parents[end] = start
    else:
        parents[start] = end


for start, end, cost in graph:
    if find(start) != find(end):
        union(start, end)
        answer += cost
        max_cost = max(cost, max_cost)

print(answer - max_cost)