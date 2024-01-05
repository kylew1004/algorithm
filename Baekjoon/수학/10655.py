# https://www.acmicpc.net/problem/10655

import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

total_dist = sum(abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in zip(points, points[1:]))
max_saved_dist = 0

for i in range(1, n - 1):
    dist_with_point = abs(points[i - 1][0] - points[i][0]) + abs(points[i - 1][1] - points[i][1]) \
                    + abs(points[i][0] - points[i + 1][0]) + abs(points[i][1] - points[i + 1][1])

    dist_without_point = abs(points[i - 1][0] - points[i + 1][0]) + abs(points[i - 1][1] - points[i + 1][1])
    
    saved_dist = dist_with_point - dist_without_point

    max_saved_dist = max(max_saved_dist, saved_dist)

print(total_dist - max_saved_dist)