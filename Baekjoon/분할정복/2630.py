# https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

num = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]
blue = 0
white = 0

def count(x, y, size):
    global blue, white
    color = graph[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if color != graph[i][j]:
                count(x, y, size // 2)
                count(x, y + size // 2, size // 2)
                count(x + size // 2, y, size // 2)
                count(x + size // 2, y + size // 2, size // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

count(0, 0, num)
print(white)
print(blue)