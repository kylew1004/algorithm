# https://www.acmicpc.net/problem/18310

import sys
input = sys.stdin.readline

n = int(input())
homes = list(map(int, input().split()))
homes.sort()

print(homes[(n-1)//2])