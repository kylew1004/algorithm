# https://www.acmicpc.net/problem/2436

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

g, l = map(int, input().split())
a = l // g
b = 1

for i in range(1, int(a ** 0.5) + 1):
    if a % i == 0:
        if gcd(i, a // i) == 1:
            b = i

print(b * g, a // b * g)