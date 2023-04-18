# https://www.acmicpc.net/problem/6497

import sys
input = sys.stdin.readline

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = [i for i in range(m)]
    graph = [list(map(int, input().split())) for _ in range(n)]
    graph.sort(key=lambda x: x[2])

    total = 0
    for a, b, c in graph:
        if find(a) != find(b):
            union(a, b)
        else:
            total += c

    print(total)