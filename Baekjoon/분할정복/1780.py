# https://www.acmicpc.net/problem/1780

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
count = [0, 0, 0]


def divide(x, y, num):
    num = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != num:
                for a in range(3):
                    for b in range(3):
                        divide(x + a * (n // 3), y + b * (n // 3), n // 3)
                return

    if num == -1:
        count[0] += 1
    elif num == 0:
        count[1] += 1
    else:
        count[2] += 1


divide(0, 0, n)
print(count[i] for i in range(3))