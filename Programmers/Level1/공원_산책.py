# https://school.programmers.co.kr/learn/courses/30/lessons/172928

from collections import deque

def solution(park, routes):
    length = len(park)
    idx = 0
    col = length
    row = len(park[0])

    for i in range(col):
        for j in range(row):
            if park[i][j] == "S":
                queue = deque([[i, j]])
                answer = [i, j]
                break

    def wall_check(x, y, nx, ny):
        for i in range(min(x, nx), max(x, nx) + 1):
            if park[i][ny] == "X":
                return True
        for j in range(min(y, ny), max(y, ny) + 1):
            if park[nx][j] == "X":
                return True
        return False

    while queue and idx < len(routes):
        x, y = queue.popleft()
        direction, cnt = routes[idx][0], int(routes[idx][2:])
        idx += 1

        if direction == "E":
            nx = x
            ny = y + cnt
        elif direction == "W":
            nx = x
            ny = y - cnt
        elif direction == "N":
            nx = x - cnt
            ny = y
        else:
            nx = x + cnt
            ny = y

        if nx < 0 or nx >= col or ny < 0 or ny >= row:
            queue.append([x, y])
        elif park[nx][ny] != "O" and park[nx][ny] != "S":
            queue.append([x, y])
        elif wall_check(x, y, nx, ny):
            queue.append([x, y])
        else:
            queue.append([nx, ny])
            answer = [nx, ny]

    return answer
