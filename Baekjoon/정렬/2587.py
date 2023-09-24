# https://www.acmicpc.net/problem/2587

import sys
input = sys.stdin.readline

arr = []
for _ in range(5):
    arr.append(int(input()))

arr.sort()
print(sum(arr) // 5)
print(arr[2])
