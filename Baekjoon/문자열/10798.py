# https://www.acmicpc.net/problem/10798

import sys
input = sys.stdin.readline

words = [input().rstrip() for _ in range(5)]

for i in range(15): 
  for j in range(5): 
    if i < len(words[j]):
        print(words[j][i], end = '')
