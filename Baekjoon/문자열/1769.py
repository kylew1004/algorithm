# https://www.acmicpc.net/problem/1769

import sys
input = sys.stdin.readline

x = input().rstrip()
cnt = 0

while len(x) > 1:
    cnt += 1
    x = str(sum(map(int, x)))
    
print(cnt)
print("YES" if int(x) % 3 == 0 else "NO")