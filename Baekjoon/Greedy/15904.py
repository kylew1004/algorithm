# https://www.acmicpc.net/problem/15904

import sys
input = sys.stdin.readline

s = input().strip()
ucpc = "UCPC"
idx = 0

for c in s:
    if c == ucpc[idx]:
        idx += 1
    if idx == 4:
        break
    
print("I love UCPC" if idx == 4 else "I hate UCPC")