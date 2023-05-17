# https://www.acmicpc.net/problem/16938
# 조합론 풀이가 근데 더 빠름

import sys
from itertools import combinations

input = sys.stdin.readline

N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))
answer = 0

problems.sort()

# 비트마스크를 이용한 풀이

for i in range(1, 1 << N):
    arr = []
    for j in range(N):
        if i & (1 << j):
            arr.append(problems[j])
    if L <= sum(arr) <= R and arr[-1] - arr[0] >= X:
        answer += 1
        
print(answer)

'''
# 조합을 이용한 풀이

for i in range(2, N + 1):
    for comb in combinations(problems, i):
        if L <= sum(comb) <= R and comb[-1] - comb[0] >= X:
            answer += 1
            
print(answer)
'''