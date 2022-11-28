# https://softeer.ai/practice/info.do?idx=1&eid=531

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
colors = {}
answer = float('inf')

for _ in range(N):
    x, y, c = map(int, input().split())
    colors[c] = colors.get(c, []) + [(x, y)]


def dfs(min_x, min_y, max_x, max_y, area, cnt):
    global answer

    if cnt == K + 1:
        if answer > area:
            answer = area
        return

    for point in colors[cnt]:
        x1, x2, y1, y2 = min_x, max_x, min_y, max_y
        if point[0] < min_x:
            x1 = point[0]
        elif point[0] > max_x:
            x2 = point[0]
        if point[1] < min_y:
            y1 = point[1]
        elif point[1] > max_y:
            y2 = point[1]

        narea = abs(x2 - x1) * abs(y2 - y1)
        if narea < answer:
            dfs(x1, y1, x2, y2, narea, cnt + 1)


for p in colors[1]:
    dfs(p[0], p[1], p[0], p[1], 0, 2)

print(answer)
