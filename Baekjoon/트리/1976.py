# https://www.acmicpc.net/problem/1976

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
        
for i in range(n):
    for j in range(n):
        if cities[i][j]:
            union(i, j)
            
for i in range(m - 1):
    if find(plan[i] - 1) != find(plan[i + 1] - 1):
        print('NO')
        break
else:
    print('YES')