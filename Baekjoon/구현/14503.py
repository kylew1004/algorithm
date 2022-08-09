# https://www.acmicpc.net/problem/14503

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph[x][y] = 2

cnt = 1

while True:
    check = False
    for _ in range(4):
        d = (d - 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                cnt += 1
                x, y = nx, ny
                check = True
                break
    if not check:
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 2:
                x, y = nx, ny
            elif graph[nx][ny] == 1:
                print(cnt)
                break
        else:
            print(cnt)
            break