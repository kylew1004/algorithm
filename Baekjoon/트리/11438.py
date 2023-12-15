# https://www.acmicpc.net/problem/4803

import sys
input = sys.stdin.readline

def dfs(v, p):
    global flag

    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(w, v)
        elif w != p:
            flag = False
            
case = 1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            flag = True
            dfs(i, 0)
            if flag:
                cnt += 1
                
    print('Case {}:'.format(case), end=' ')
    if cnt == 0:
        print('No trees.')
    elif cnt == 1:
        print('There is one tree.')
    else:
        print('A forest of {} trees.'.format(cnt))
    case += 1