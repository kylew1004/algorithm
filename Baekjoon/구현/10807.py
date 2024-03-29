# https://www.acmicpc.net/problem/10807

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
v = int(input())

answer = 0
for i in arr:
    if i == v:
        answer += 1
        
print(answer)