# https://www.acmicpc.net/problem/1929

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            return False
    return True

for i in range(n, m + 1):
    if is_prime(i):
        print(i)