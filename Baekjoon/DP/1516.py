# https://www.acmicpc.net/problem/1516

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
time = [0] * n
graph = [[] for _ in range(n)]
indegree = [0] * n

for i in range(n):
    time[i] = arr[i][0]
    for j in range(1, len(arr[i])-1):
        graph[arr[i][j]-1].append(i)
        indegree[i] += 1
        
def topology_sort():
    result = time[:]
    q = []
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.pop(0)
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i)

topology_sort()