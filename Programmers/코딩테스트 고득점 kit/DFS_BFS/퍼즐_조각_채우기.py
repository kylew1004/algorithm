# https://school.programmers.co.kr/learn/courses/30/lessons/84021

from copy import deepcopy

def solution(game_board, table):
    answer = 0
    blank = []
    length = len(game_board)
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    

    def dfs(board, x, y, position, num):
        result = [position]
        board[x][y] = -1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < length and 0 <= ny and ny < length:
                if board[nx][ny] == num:
                    result += dfs(board, nx, ny, [position[0] + dx[i], position[1] + dy[i]], num)

        return result
    
    
    def rotate(table):
        rotated = [[0] * length for _ in range(length)]
        for i in range(length):
            for j in range(length):
                rotated[j][length - i - 1] = table[i][j]

        return rotated
    
    
    for i in range(length):
        for j in range(length):
            if game_board[i][j] == 0:
                blank.append(dfs(game_board, i, j, [0, 0], 0))

    for _ in range(4):
        table = rotate(table)
        ntable = deepcopy(table)
        for i in range(length):
            for j in range(length):
                if ntable[i][j] == 1:
                    block = dfs(ntable, i, j, [0, 0], 1)
                    if block in blank:
                        blank.remove(block)
                        answer += len(block)
                        table = deepcopy(ntable)
                    else:
                        ntable = deepcopy(table)

    return answer