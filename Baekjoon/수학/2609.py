# https://www.acmicpc.net/problem/2609

import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())

def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)
    
def get_lcm(a, b):
    return a * b // gcd

gcd = get_gcd(n1, n2)
lcm = get_lcm(n1, n2)

print(gcd)
print(lcm)