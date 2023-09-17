# https://www.acmicpc.net/problem/10872

import sys
input = sys.stdin.readline

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input())
print(factorial(n))
