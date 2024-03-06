# https://www.acmicpc.net/problem/9020

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    sieve = [False, False] + [True] * (n - 1)

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(2 * i, n + 1, i):
                sieve[j] = False

    for i in range(n // 2, 1, -1):
        if sieve[i] and sieve[n - i]:
            print(i, n - i)
            break