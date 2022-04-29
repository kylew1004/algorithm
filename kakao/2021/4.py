# https://tech.kakao.com/2021/07/08/2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-for-tech-developers-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%B4%EC%84%A4/

import queue

INF = 987654321

def dijkstra(n, graph, src, dst, traps):
    pq = queue.PriorityQueue()
    visited = [[False for _ in range(1<<len(traps))] for _ in range(n+1)]
    pq.put((0, src, 0))
    
    while not pq.empty():
        curr = pq.get()
        w = curr[0]
        u = curr[1]
        state = curr[2]

        if u == dst:
            return w
        if visited[u][state]:
            continue
        visited[u][state] = True

        currTrapped = False
        trapped = {}
        for i in range(len(traps)):
            bit = 1 << i
            if state & bit:
                if traps[i] == u:
                    state &= ~bit               # 반전연산
                else:
                    trapped[traps[i]] = True
            else:
                if traps[i] == u:
                    state |= bit
                    trapped[traps[i]] = True
                    currTrapped = True
                    
        for v in range(1, n+1):
            if v == u:
                continue
            nextTrapped = True if v in trapped else False
            if currTrapped == nextTrapped:
                if graph[u][v] != INF:
                    pq.put((w + graph[u][v], v, state))
            else:
                if graph[v][u] != INF:
                    pq.put((w + graph[v][u], v, state))
    return INF
            


def solution(n, start, end, roads, traps):
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0
        
    for data in roads:
        u = data[0]
        v = data[1]
        w = data[2]
        if w < graph[u][v]:
            graph[u][v] = w

    return dijkstra(n, graph, start, end, traps)
