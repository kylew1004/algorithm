# https://www.acmicpc.net/problem/2475

import sys
input = sys.stdin.readline


num = list(map(int, input().split()))
result = 0

for i in num:
    result += i ** 2

print(result % 10)