# https://www.acmicpc.net/problem/14889

import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())

stat_matrix = [list(map(int, input().split())) for _ in range(N)]
number_list = []
score_list = []
all_list = [i for i in range(1,N+1)]


def dfs():
    if len(number_list) == N / 2:
        start = 0
        link = 0
        another_list = list(set(all_list)-set(number_list))

        for j in combinations(number_list, 2):
            start = start + stat_matrix[j[0] - 1][j[1] - 1] + stat_matrix[j[1] - 1][j[0] - 1]
        for k in combinations(another_list, 2):
            link = link + stat_matrix[k[0] - 1][k[1] - 1] + stat_matrix[k[1] - 1][k[0] - 1]
        score_list.append(abs(start - link))
        return

    for i in range(1, N + 1):
        if i in number_list:
            continue
        if i not in number_list:
            if len(number_list) == 0:
                number_list.append(i)
                dfs()
                number_list.pop()
            elif i > number_list[-1]:
                number_list.append(i)
                dfs()
                number_list.pop()

dfs()
print(min(score_list))