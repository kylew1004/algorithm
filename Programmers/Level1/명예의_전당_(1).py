# https://school.programmers.co.kr/learn/courses/30/lessons/138477

import heapq

def solution(k, score):
    answer = []
    board = []
    flag = False

    for s in score:
        heapq.heappush(board, s)
        if flag:
            heapq.heappop(board)
        else:
            if len(board) == k:
                flag = True
        answer.append(board[0])

    return answer