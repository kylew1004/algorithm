# https://www.acmicpc.net/problem/23253

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = 'Yes'

for _ in range(m):
    k = int(input().rstrip())
    books = list(map(int, input().split()))
    
    if books != sorted(books, reverse=True):
        result = 'No'

print(result)