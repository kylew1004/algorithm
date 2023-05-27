# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0
for i in range(n):
    if end <= time[i][0]:
        end = time[i][1]
        cnt += 1
print(cnt)