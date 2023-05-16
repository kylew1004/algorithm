# https://www.acmicpc.net/problem/15661
# 엄청난 노가다 끝에 겨우 푼 문제, 결국 pypy3로 통과했다.

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')

def calculate_stat(team):
    stat = 0
    for i in team:
        for j in team:
            stat += s[i][j]
    return stat

cases = []
for i in range(1, n // 2 + 1):
    cases += list(combinations(range(n), i))

for case in cases:
    team = list(case)
    stat = calculate_stat(team)
    answer = min(answer, abs(stat - calculate_stat(list(set(range(n)) - set(team)))))

print(answer)