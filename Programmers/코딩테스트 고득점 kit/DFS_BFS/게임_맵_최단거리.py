# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque
from copy import deepcopy

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    graph = deepcopy(maps)
    height = len(maps) - 1
    width = len(maps[0]) - 1
    queue = deque()
    queue.append([0, 0, 1])
    
    while queue:
        x, y, cnt = queue.popleft()

        for i in range(4):
            if x + dx[i] > height or x + dx[i] < 0 or y + dy[i] > width or y + dy[i] < 0 or graph[x + dx[i]][y + dy[i]] == 0:
                continue
            if graph[x + dx[i]][y + dy[i]] == 2:
                continue
            if x + dx[i] == height and y + dy[i] == width:
                return cnt + 1
            queue.append([x + dx[i], y + dy[i], cnt + 1])
            graph[x + dx[i]][y + dy[i]] = 2

    return -1