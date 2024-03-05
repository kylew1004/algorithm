# https://www.acmicpc.net/problem/1058

import sys
input = sys.stdin.readline

n = int(input())
friends = [list(input()) for _ in range(n)]
answer = 0
relations = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if friends[i][j] == "Y" or (friends[i][k] == "Y" and friends[k][j] == "Y"):
                relations[i][j] = 1

for row in relations:
    answer = max(answer, sum(row))

print(answer)