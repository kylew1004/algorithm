# https://www.acmicpc.net/problem/4386

def prim(s, n, distance):
    visited = [0 for _ in range(n)]
    cost = [float('inf') for _ in range(n)]
    cost[s] = 0

    for _ in range(n):
        minidx, minval = 0, float('inf')
        for j in range(n):
            if not visited[j] and cost[j] < minval:
                minidx = j
                minval = cost[j]
        visited[minidx] = 1

        for j in range(n):
            if visited[j] or j == minidx:
                continue
            cost[j] = min(cost[j], distance[minidx][j])

    return sum(cost)

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
distance = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        d = ((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** (1/2)
        distance[i][j] = d
        distance[j][i] = d

print(prim(0, n, distance))