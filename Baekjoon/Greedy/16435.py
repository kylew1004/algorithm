# https://www.acmicpc.net/problem/16435

import sys
input = sys.stdin.readline

cnt, n = map(int, input().split())
fruits = list(map(int, input().split()))
fruits.sort()

for i in fruits:
    if i <= n:
        n += 1
        
print(n)