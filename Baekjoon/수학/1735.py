# https://www.acmicpc.net/problem/1735

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())
gcd_num = gcd(a * d + b * c, b * d)

print((a * d + b * c) // gcd_num, (b * d) // gcd_num)