# https://www.acmicpc.net/problem/2752

import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
arr.sort()

print(*arr)