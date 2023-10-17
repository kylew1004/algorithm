# https://www.acmicpc.net/problem/11501

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    info = list(map(int, input().split()))
    stack = []
    top = info[-1]
    result = 0

    for i in range(n - 1, -1, -1):
        if info[i] > top:
            top = info[i]
        else:
            result += top - info[i]

    print(result)