# https://www.acmicpc.net/problem/24416
# 문제 조건 그대로 풀면 시간초과가 난다.

import sys
input = sys.stdin.readline

def fib(n):
    cnt = 1
    a, b = 0, 1
    while cnt < n:
        a, b = b, a + b
        cnt += 1
    return b

def fibonacci(n):
    return n - 2


n = int(input())
print(fib(n), fibonacci(n))