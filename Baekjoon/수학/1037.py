# https://www.acmicpc.net/problem/1037

import sys
input = sys.stdin.readline

n = int(input())
divisors = list(map(int, input().split()))

print(max(divisors) * min(divisors))