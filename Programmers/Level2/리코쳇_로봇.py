# https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def solution(board):
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                a, b = i, j
                break
    
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    flag = False
    queue = deque()
    queue.append([a, b, 0])
    
    while queue:
        x, y, cnt = queue.popleft()

        visited[x][y] = True
        
        if board[x][y] == "G":
            flag = True
            break
        for i in range(4):
            nx, ny = x, y
            while nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0]) and board[nx][ny] != "D":
                nx += dx[i]
                ny += dy[i]
            if dx[i] > 0:
                nx -= 1
            elif dx[i] < 0:
                nx += 1
            elif dy[i] > 0:
                ny -= 1
            elif dy[i] < 0:
                ny += 1

            if visited[nx][ny]:
                continue
            queue.append([nx, ny, cnt + 1])

    answer = cnt if cnt != 0 and flag else -1
    
    return answer

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))