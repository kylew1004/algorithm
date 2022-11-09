# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
answer = float('inf')
houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            houses.append([i, j])
        elif board[i][j] == 2:
            chickens.append([i, j])

for chicken in combinations(chickens, m):
    tmp = 0
    for house in houses:
        distance = 100
        for j in range(m):
            distance = min(distance, abs(house[0] - chicken[j][0]) + abs(house[1] - chicken[j][1]))
        tmp += distance
    answer = min(answer, tmp)

print(answer)
