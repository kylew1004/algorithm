# https://www.acmicpc.net/problem/10825

import sys
input = sys.stdin.readline

n = int(input())
info = []

for _ in range(n):
    name, kor, eng, math = input().split()
    info.append([name, int(kor), int(eng), int(math)])

info.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in info:
    print(i[0])