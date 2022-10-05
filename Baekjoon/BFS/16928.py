# https://www.acmicpc.net/problem/16928

from collections import deque

n, m = map(int, input().split())

board = [0] * 101
visited = [False] * 101
ladder = dict()
snake = dict()

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

queue = deque([1])

while queue:
    q = queue.popleft()

    if q == 100:
        print(board[q])
        break

    for dice in range(1, 7):
        next_place = q + dice
        if next_place <= 100 and not visited[next_place]:
            if next_place in ladder.keys():
                next_place = ladder[next_place]
            if next_place in snake.keys():
                next_place = snake[next_place]
            if not visited[next_place]:
                visited[next_place] = True
                board[next_place] = board[q] + 1
                queue.append(next_place)
