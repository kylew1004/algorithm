# https://school.programmers.co.kr/learn/courses/30/lessons/86052

def solution(grid):
    answer = []
    graph = [list(g) for g in grid]
    row = len(grid)
    col = len(grid[0])
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]


    for x in range(row):
        for y in range(col):
            for direction in range(4):
                cnt = 0
                if visited[x][y][direction]:
                    continue
                while True:
                    visited[x][y][direction] = True
                    if graph[x][y] == "L":
                        direction = (direction + 1) % 4
                    elif graph[x][y] == "R":
                        direction = (direction + 3) % 4
                    x = (x + dx[direction]) % row
                    y = (y + dy[direction]) % col
                    cnt += 1
                    if visited[x][y][direction]:
                        answer.append(cnt)
                        break

    answer.sort()

    return answer