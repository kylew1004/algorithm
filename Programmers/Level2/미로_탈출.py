# https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 시간 초과로 애를 먹은 문제
# queue에 이동한 횟수까지 넣어서 계산하니 시간 초과가 났다. visited로 시간을 계산해서 해결했다.

from collections import deque

def bfs(maps, x, y, target, cnt, row, col):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[0] * col for _ in range(row)]
    flag = False
    
    queue = deque()
    queue.append([x, y])
    visited[x][y] = cnt
    
    while queue:
        x, y = queue.popleft()
        if maps[x][y] == target:
            flag = True
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue
            if visited[nx][ny] != 0 or maps[nx][ny] == "X":
                continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append([nx, ny])
    
    return [x, y, flag, visited[x][y]]


def solution(maps):
    row = len(maps)
    col = len(maps[0])
    stop = False
    for i in range(row):
        if stop:
            break
        for j in range(col):
            if maps[i][j] == "S":
                x, y = i, j
                stop = True
                break

    x, y, flag, cnt = bfs(maps, x, y, "L", 0, row, col)
    if flag == False:
        return -1
    x, y, flag, cnt = bfs(maps, x, y, "E", cnt, row, col)
    if flag == False:
        return -1
    else:
        return cnt
