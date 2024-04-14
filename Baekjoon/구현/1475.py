# https://www.acmicpc.net/problem/1475

import sys
input = sys.stdin.readline

n = input().rstrip()
counter = [0] * 10

for i in n:
    counter[int(i)] += 1
    
counter[6] = (counter[6] + counter[9] + 1) // 2
counter[9] = 0

print(max(counter))