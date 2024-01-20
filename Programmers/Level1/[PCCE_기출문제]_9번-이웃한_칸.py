# https://school.programmers.co.kr/learn/courses/30/lessons/250125?language=python3

def solution(board, h, w):
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    n = len(board)
    count = 0
    color = board[h][w]
    
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if nh >= n or nh < 0 or nw >= n or nw < 0:
            continue
        if board[nh][nw] == color:
            count += 1

    return count
