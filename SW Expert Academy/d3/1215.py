# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE&problemTitle=%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=3

for tc in range(1, 11):
    length = int(input())
    board = []
    for i in range(8):
        board.append(input())

    count = 0

    for i in range(8):
        for j in range(9 - length):
            answer = 1
            for k in range(length // 2):
                if board[i][j+k] == board[i][j + length - k - 1]:
                    answer *= 1
                else :
                    answer *= 0
            if answer == 1:
                count += 1

    for i in range(9 - length):
        for j in range(8):
            answer = 1
            for k in range(length//2):
                if board[i + k][j] == board[i + length - k - 1][j]:
                    answer *= 1
                else :
                    answer *= 0
            if answer == 1:
                count += 1

    print("#{} {}".format(tc, count))