# https://www.acmicpc.net/problem/14469

import sys
input = sys.stdin.readline

n = int(input())
cow = [list(map(int, input().split())) for _ in range(n)]
cow.sort(key=lambda x: x[0])

time = 0

for i in range(n):
    if time < cow[i][0]:
        time = cow[i][0] + cow[i][1]
    else:
        time += cow[i][1]

print(time)