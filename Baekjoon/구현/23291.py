# https://www.acmicpc.net/problem/23291

from collections import deque

n, k = map(int, input().split())
board = [deque(list(map(int,input().split())))]
moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
answer = 0


def add_fish():
    num = min(board[0])
    
    for i in range(len(board[0])):
        if board[0][i] == num:
            board[0][i] += 1


def rotate_90(block):
    tmp = [[0] * len(block) for _ in range(len(block[0]))]
    for i in range(len(block[0])) :
        for j in range(len(block)) :
            tmp[i][j] = block[j][len(block[0])-1-i]
    return tmp


def rotate_180(graph) :
    tmp = []
    for i in reversed(range(len(graph))) :
        graph[i].reverse()
        tmp.append(graph[i])

    return tmp


def rotate_pot(graph):
    while True :
        if len(graph) > len(graph[0]) - len(graph[-1]) :
            break
        blocks = []
        r = len(graph)
        c = len(graph[-1])

        for i in range(r) :
            tmp_q = deque()
            for _ in range(c) :
                tmp_q.append(graph[i].popleft())
            blocks.append(tmp_q)

        graph = [graph[0]]
        rotated = rotate_90(blocks)
        for row in rotated :
            graph.append(deque(row))

    return graph

    
def fix_fish(graph) :
    dp = [[0] * len(graph[x]) for x in range(len(graph))]
    for x in range(len(graph)) :
        for y in range(len(graph[x])) :
            for move in moves :
                nx = x + move[0]
                ny = y + move[1]

                if 0 <= nx < len(graph) and 0 <= ny < len(graph[nx]) :
                    if graph[x][y] > graph[nx][ny] :
                        diff = (graph[x][y] - graph[nx][ny]) // 5
                        if diff >= 1 :
                            dp[x][y] -= diff
                    else :
                        diff = (graph[nx][ny] - graph[x][y]) // 5
                        if diff >= 1 :
                            dp[x][y] += diff
    for i in range(len(graph)) :
        for j in range(len(graph[i])) :
            graph[i][j] += dp[i][j]


def make_one_line(graph) :
    tmp = deque()
    for i in range(len(graph[-1])) :
        for j in range(len(graph)) :
            tmp.append(graph[j][i])

    for i in range(len(graph[-1]), len(graph[0])) :
        tmp.append(graph[0][i])

    return [tmp]


def half_rotation(graph) :
    tmp = deque()
    for i in range(n // 2) :
        tmp.append(graph[0].popleft())
    rotated = rotate_180([tmp])
    graph += rotated

    left = []
    for i in range(2) :
        data = deque()
        for j in range(n // 4) :
            data.append(graph[i].popleft())
        left.append(data)
    rotated = rotate_180(left)
    graph += rotated


while True :
    diff = max(board[0]) - min(board[0])
    if diff <= k :
        print(answer)
        break

    add_fish()

    value = board[0].popleft()
    board.append(deque([value]))

    board = rotate_pot(board)

    fix_fish(board)

    board = make_one_line(board)

    half_rotation(board)

    fix_fish(board)

    board = make_one_line(board)

    answer += 1
