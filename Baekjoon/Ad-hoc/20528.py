# https://www.acmicpc.net/problem/20528

import sys
input = sys.stdin.readline

n = int(input())
words = input().split()

for i in range(n-1):
    if words[i][0] != words[i+1][0]:
        print(0)
        sys.exit()

print(1)