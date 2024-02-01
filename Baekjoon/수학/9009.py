# https://www.acmicpc.net/problem/9009

import sys
input = sys.stdin.readline

t = int(input())
fibonacci = [0, 1]
for i in range(2, 46):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    
for _ in range(t):
    n = int(input())
    result = []
    for i in range(45, -1, -1):
        if fibonacci[i] <= n:
            result.append(fibonacci[i])
            n -= fibonacci[i]
    result.sort()
    print(*result[1:])
    
    