# https://school.programmers.co.kr/learn/courses/30/lessons/12905

def solution(board): 
    answer = 0

    if len(board) < 2 and 1 in sum(board, []): 
        return 1

    for i in range(1, len(board)): 
        for j in range(1, len(board[i])): 
            if board[i][j]: 
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1 
                answer = max(answer, board[i][j])

    return answer ** 2
