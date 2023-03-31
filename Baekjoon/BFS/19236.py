# https://www.acmicpc.net/problem/19236

from collections import deque
from copy import deepcopy

graph = [[] for _ in range(4)]
fish = {i: [] for i in range(1, 17)}
survived = [True] * 17
moves = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
answer = 0

for i in range(4):
    info = list(map(int, input().split()))
    for j in range(4):
        fish[info[2 * j]] = [i, j, info[2 * j + 1] - 1]
        graph[i].append(info[2 * j])


def move_fish(graph, fish, survived):
    for i in range(1, 17):
        if not survived[i]:
            continue
        x, y, direction = fish[i]
        nx, ny = x + moves[direction][0], y + moves[direction][1]
        while not (0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny] != -1):
            direction = (direction + 1) % 8
            nx, ny = x + moves[direction][0], y + moves[direction][1]
        if graph[nx][ny] != 0:
            fish[graph[nx][ny]][0], fish[graph[nx][ny]][1] = x, y
        fish[i] = [nx, ny, direction]
        graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]


def move_shark(x ,y, cnt):
    nx, ny = x + moves[shark_direction][0] * cnt, y + moves[shark_direction][1] * cnt
    if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny] != 0:
        return nx, ny
    else:
        return -1, -1


queue = deque([[0, 0, 0, deepcopy(graph), deepcopy(fish), deepcopy(survived)]])

while queue:
    x, y, eaten, graph, fish, survived = queue.popleft()
    eaten += graph[x][y]
    survived[graph[x][y]] = False
    shark_direction = fish[graph[x][y]][2]
    graph[x][y] = -1
    answer = max(answer, eaten)
    move_fish(graph, fish, survived)

    for i in range(1, 4):
        nx, ny = move_shark(x, y, i)
        if nx != -1:
            new_graph = deepcopy(graph)
            new_graph[x][y] = 0
            queue.append([nx, ny, eaten, new_graph, deepcopy(fish), deepcopy(survived)])

print(answer)