# https://school.programmers.co.kr/learn/courses/30/lessons/160585
# 예외처리가 생각보다 까다로웠다. 단순히 승패 횟수 및 OX를 세는 경우만 생각했는데, 승패에 따른 OX 개수를 세는 것도 고려해야 했다.

def solution(board):
    def check_winner(target):
        for row in board:
            if list(row) == [target, target, target]:
                return True
        
        for j in range(3):
            if [board[0][j], board[1][j], board[2][j]] == [target, target, target]:
                return True
        
        if ([board[0][0], board[1][1], board[2][2]] == [target, target, target]):
            return True
        if ([board[0][2], board[1][1], board[2][0]] == [target, target, target]):
            return True
        
        return False
    
    
    cnt_o = 0
    cnt_x = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                cnt_o += 1
            elif board[i][j] == "X":
                cnt_x += 1
    if not (cnt_o == cnt_x or cnt_o == cnt_x + 1):
        return 0
    if check_winner("O") and check_winner("X"):
        return 0
    if check_winner("O") and cnt_o != cnt_x + 1:
        return 0
    if check_winner("X") and cnt_o != cnt_x:
        return 0

    
    return 1