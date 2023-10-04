# https://www.acmicpc.net/problem/1212

import sys
input = sys.stdin.readline

num = input().rstrip()
answer = bin(int(num, 8))[2:]
print(answer)
