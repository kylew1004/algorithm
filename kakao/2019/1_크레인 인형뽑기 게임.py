# https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3

def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] != 0:
                basket.append(board[i][m - 1])
                board[i][m - 1] = 0
                break
        if len(basket) > 1 and basket[-1] == basket[-2]:
            answer += 2
            basket = basket[0:-2]
    return answer
