# https://www.acmicpc.net/problem/10775

import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y
    
G = int(input())
P = int(input())
parent = [i for i in range(G + 1)]
cnt = 0

for _ in range(P):
    g = int(input())
    docking = find(g)
    if docking == 0:
        break
    union(docking, docking - 1)
    cnt += 1
    
print(cnt)