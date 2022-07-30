# https://www.acmicpc.net/problem/14502

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
tmp = [[0] * m for _ in range(n)]
result = 0

def virus(x,y):
    for i in range(4):
        nx = x + moves[i][0]
        ny = y + moves[i][1]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if tmp[nx][ny]==0:
                tmp[nx][ny] = 2
                virus(nx, ny)

def score():
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)
        result = max(result, score())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)