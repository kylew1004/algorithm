# https://www.acmicpc.net/problem/2750

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
for a in arr:
    print(a)