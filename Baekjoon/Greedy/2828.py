# https://www.acmicpc.net/problem/2828

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
i = int(input())
start = 1
end = m
cnt = 0

for _ in range(i):
    apple = int(input())
    if apple > end:
        cnt += apple - end
        start += apple - end
        end = apple
    elif apple < start:
        cnt += start - apple
        end -= start - apple
        start = apple

print(cnt)