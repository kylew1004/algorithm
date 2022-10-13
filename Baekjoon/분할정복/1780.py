# https://www.acmicpc.net/problem/1780

import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
count = [0, 0, 0]


def divide(x, y, num):
    global count
    visited = graph[x][y]

    for i in range(x, x + num):
        for j in range(y, y + num):
            if graph[i][j] != visited:
                for a in range(3):
                    for b in range(3):
                        divide(x + a * num // 3, y + b * num // 3, num // 3)
                return

    if visited == -1:
        count[0] += 1
    elif visited == 0:
        count[1] += 1
    else:
        count[2] += 1


divide(0, 0, n)
[print(i) for i in count]