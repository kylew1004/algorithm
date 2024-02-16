# https://www.acmicpc.net/problem/2702

import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a, b), gcd(a, b))