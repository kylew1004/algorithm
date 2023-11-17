# https://www.acmicpc.net/problem/1431

import sys
input = sys.stdin.readline

n = int(input())
serial = [input().strip() for _ in range(n)]

serial.sort(key=lambda x: (len(x), sum(int(i) for i in x if i.isdigit()), x))

for s in serial:
    print(s)