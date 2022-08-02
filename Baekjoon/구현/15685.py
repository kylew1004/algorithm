# https://www.acmicpc.net/problem/15685

n = int(input())
moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]
graph = [[0] * 101 for _ in range(101)]

for i in range(n):
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1
    tmp = [d]
    q = [d]
    for _ in range(g + 1):
        for idx in q:
            x += moves[idx][0]
            y += moves[idx][1]
            graph[x][y] = 1
        q = [(i + 1) % 4 for i in tmp]
        q.reverse()
        tmp = tmp + q

result = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i][j + 1] and graph[i + 1][j] and graph[i + 1][j + 1]:
            result += 1
print(result)
