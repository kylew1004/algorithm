# https://www.acmicpc.net/problem/1059

import sys
input = sys.stdin.readline

l = int(input().rstrip())
s = list(map(int, input().split()))
n = int(input().rstrip())

s.sort()
if n in s:
    print(0)
else:
    min = 0
    max = 0
    for num in s:
        if num < n:
            min = num
        elif num > n and max == 0:
            max = num
    max -= 1
    min += 1
    print((max - n + 1) * (n - min) + (max - n))
