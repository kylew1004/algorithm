# https://www.acmicpc.net/problem/11653

import sys
input = sys.stdin.readline

n = int(input())
i = 2

while n > 1:
    if n % i == 0:
        print(i)
        n //= i
    else:
        i += 1
