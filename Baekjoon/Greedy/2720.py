# https://www.acmicpc.net/problem/2720

import sys
input = sys.stdin.readline

t = int(input())
arr = []

def change(n):
    result = []
    coin = [25, 10, 5, 1]
    
    for i in coin:
        result.append(n // i)
        n = n % i
    
    return ' '.join(map(str, result))
    
for _ in range(t):
    n = int(input())
    arr.append(change(n))
    
for i in arr:
    print(i)