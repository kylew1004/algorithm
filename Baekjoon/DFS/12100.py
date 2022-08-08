# https://www.acmicpc.net/problem/12100

from copy import deepcopy

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def move(graph, dir):
    if dir == 0:            # 동쪽
        for i in range(n):
            criteria = n - 1
            for j in range(n - 2, -1, -1):
                if graph[i][j]:
                    tmp = graph[i][j]
                    graph[i][j] = 0
                    if graph[i][criteria] == 0:
                        graph[i][criteria] = tmp
                    elif graph[i][criteria] == tmp:
                        graph[i][criteria] = tmp * 2
                        criteria -= 1
                    else:
                        criteria -= 1
                        graph[i][criteria] = tmp

    elif dir == 1:          # 서쪽
        for i in range(n):
            criteria = 0
            for j in range(1, n):
                if graph[i][j]:
                    tmp = graph[i][j]
                    graph[i][j] = 0
                    if graph[i][criteria] == 0:
                        graph[i][criteria] = tmp
                    elif graph[i][criteria] == tmp:
                        graph[i][criteria] = tmp * 2
                        criteria += 1
                    else:
                        criteria += 1
                        graph[i][criteria] = tmp

    elif dir == 2:          # 남쪽
        for j in range(n):
            criteria = n - 1
            for i in range(n - 2, -1, -1):
                if graph[i][j]:
                    tmp = graph[i][j]
                    graph[i][j] = 0
                    if graph[criteria][j] == 0:
                        graph[criteria][j] = tmp
                    elif graph[criteria][j] == tmp:
                        graph[criteria][j] = tmp * 2
                        criteria -= 1
                    else:
                        criteria -= 1
                        graph[criteria][j] = tmp

    else:                   # 북쪽
        for j in range(n):
            criteria = 0
            for i in range(1, n):
                if graph[i][j]:
                    tmp = graph[i][j]
                    graph[i][j] = 0
                    if graph[criteria][j] == 0:
                        graph[criteria][j] = tmp
                    elif graph[criteria][j] == tmp:
                        graph[criteria][j] = tmp * 2
                        criteria += 1
                    else:
                        criteria += 1
                        graph[criteria][j] = tmp

    return graph
        
def dfs(cnt, graph):
    global answer
    
    if cnt == 5:
        for x in range(n):
            for y in range(n):
                answer = max(answer, graph[x][y])
    else:
        for dir in range(4):
            tmp_graph = move(deepcopy(graph), dir)
            dfs(cnt + 1, tmp_graph)
                

dfs(0, graph)
print(answer)