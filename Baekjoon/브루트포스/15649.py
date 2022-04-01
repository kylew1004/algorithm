# https://www.acmicpc.net/problem/15649

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * N
lst = []

def DFS(depth):
    if depth == M:
        print(' '.join(map(str, lst)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            lst.append(i+1)
            DFS(depth+1)
            visited[i] = False
            lst.pop()
DFS(0)