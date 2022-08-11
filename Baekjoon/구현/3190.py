# https://www.acmicpc.net/problem/3190

from collections import deque

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
k = int(input())
for i in range(k):
    apple_x, apple_y = map(int, input().split())
    graph[apple_x - 1][apple_y - 1] = 2
l = int(input())
times = {}
for i in range(l):
    x, c = input().split()
    times[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 0
direction = 0
queue = deque()
queue.append((0, 0))

def turn(alpha):
    global direction

    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in times:
            turn(times[cnt])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in times:
            turn(times[cnt])

    else:
        break

print(cnt)