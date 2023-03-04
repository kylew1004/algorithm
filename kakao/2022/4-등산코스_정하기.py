import heapq

def solution(n, paths, gates, summits):
    answer = []
    graph = {i : [] for i in range(1, n + 1)}

    for start, end, dist in paths:
        graph[start].append((end, dist))
        graph[end].append((start, dist))

    for gate in gates:
        costs[gate] = 0
        dij.append((0, gate))

    costs = [10000001 for _ in range(n + 1)]
    dij = []


    while dij:
        d, node = heapq.heappop(dij)

        if costs[node] < d:
            continue

        if node in summits:
            answer.append([costs[node], node])
            continue

        for next, dist in graph[node]:
            added_dist = max(costs[node], dist)
            if added_dist < costs[next]:
                costs[next] = added_dist
                heapq.heappush(dij, (costs[next], next))

    answer.sort()
    return [answer[0][1], answer[0][0]]


print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))




'''
# 처음 풀이
# 시간초과로 쓰지 못함, heapq를 사용해야함

from collections import deque
    
def solution(n, paths, gates, summits):
    answer = []

    graph = {}
    costs = {}
    
    for start, end, cost in paths:
        graph[start] = graph.get(start, []) + [[end, cost]]
        graph[end] = graph.get(end, []) + [[start, cost]]

    for summit in summits:
        costs[summit] = costs.get(summit, 10000001)


    def find(start):
        costs_node = [0] * (n + 1)
        costs_node[start] = 1
        queue = deque([[start, 0, costs_node]])

        while queue:
            q, cost, costs = queue.popleft()

            if q in summits:
                costs[q] = min(costs[q], cost)
                continue

            for node, ncost in graph[q]:
                if costs[node] == 0:
                    ncosts = costs[:]
                    ncosts[node] = 1
                    ncost = max(ncost, cost)
                    queue.append([node, ncost, ncosts])

    for gate in gates:
        find(gate)
    costs = sorted(costs.items(), key = lambda x : (x[1], x[0]))

    answerwer = costs[0]
    return answer
'''