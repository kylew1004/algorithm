# https://www.acmicpc.net/problem/2885

import sys
input = sys.stdin.readline

k = int(input())
n = 1
cnt = 0

while n < k:
    n *= 2

answer = n

while k > 0:
    if k >= n:
        k -= n
    else:
        n //= 2
        cnt += 1

print(answer, cnt)
