# https://www.acmicpc.net/problem/1201

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

if n < m + k - 1 or n > m * k:
    print(-1)
else:
    arr = list(range(k, 0, -1))
    n -= k
    m -= 1
    while m:
        arr.extend(range(k + n // m, k, -1))
        k += n // m
        n -= n // m
        m -= 1
    print(*arr)