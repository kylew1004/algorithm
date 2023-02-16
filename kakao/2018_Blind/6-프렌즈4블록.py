# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def remake_board(m, n, board, removed):
    new_board = [['0'] * n for _ in range(m)]

    for i in range(n):
        idx1 = m - 1    # board index
        idx2 = m - 1    # new_board index
        while idx1 >= 0:
            if removed[idx1][i] == 0:
                new_board[idx2][i] = board[idx1][i]
                idx2 -= 1
            idx1 -= 1

    return new_board


def solution(m, n, board):
    answer = 0

    flag = True
    while flag:
        removed = [[0] * n for _ in range(m)]
        flag = False
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == '0':
                    continue
                if board[i][j] == board[i + 1][j] and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j + 1]:
                    removed[i][j], removed[i + 1][j], removed[i][j + 1], removed[i + 1][j + 1] = 1, 1, 1, 1
                    flag = True
        if not flag:
            break
        else:
            board = remake_board(m, n, board, removed)
            for i in range(m):
                answer += removed[i].count(1)

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))