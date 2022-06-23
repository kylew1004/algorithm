# https://www.acmicpc.net/problem/14499

import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = []
dist = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
dice, temp = [0]*6, [0]*6
for i in range(n):
    graph.append(list(map(int, input().split())))
orders = list(map(int, input().split()))
direction = [
    (2, 0, 5, 3, 4, 1),
    (1, 5, 0, 3, 4, 2),
    (4, 1, 2, 0, 5, 3),
    (3, 1, 2, 5, 0, 4)
]

for order in orders:
    order -= 1
    x, y = x + dx[order], y + dy[order]
    if x < 0 or x >= n or y < 0 or y >= m:
        x, y = x - dx[order], y - dy[order]
        continue
    for idx in range(6):
        temp[idx] = dice[idx]
    for idx in range(6):
        dice[idx] = temp[direction[order][idx]]
    if graph[x][y]:
        dice[5] = graph[x][y]
        graph[x][y] = 0
    else:
        graph[x][y] = dice[5]
    print(dice[0])