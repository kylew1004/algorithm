# https://www.acmicpc.net/problem/23288
# 이 문제는 예시를 잘 읽어봐야한다. 예시2를 보면 2가 북쪽에 있기 때문에 주사위를 남쪽방향으로 돌렸을 때 정면이 와야한다는 것을 캐치해야한다.
# 문제를 꼼꼼히 읽어봐야 캐치할 수 있는 부분.

from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dice = [2, 1, 5, 6, 4, 3]
answer = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 남북은 전개도가 반대로

def rotate():
    if dir == 0: # 동
        dice[1], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[3], dice[1]
    elif dir == 1: # 남
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif dir == 2: # 서
        dice[1], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[1], dice[3]
    elif dir == 3: # 북
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]


def bfs(r, c):
    queue = deque([(r, c)])
    visited = [[False] * m for _ in range(n)]
    point = 1
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == graph[r][c]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    point += 1

    return point


x, y, dir = 0, 0, 0

for _ in range(k):
    nx, ny = x + dx[dir], y + dy[dir]
    if not (0 <= nx < n and 0 <= ny < m):
        dir = (dir + 2) % 4
        x, y = x + dx[dir], y + dy[dir]
    else:
        x, y = nx, ny
    answer += (graph[x][y] * bfs(x, y))
    rotate()

    if graph[x][y] < dice[3]:
        dir = (dir + 1) % 4
    elif graph[x][y] > dice[3]:
        dir = (dir + 3) % 4


print(answer)