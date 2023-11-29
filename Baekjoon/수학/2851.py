# https://www.acmicpc.net/problem/2581

import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

arr = [True] * (n + 1)
arr[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if arr[i]:
        for j in range(i * 2, n + 1, i):
            arr[j] = False
            
prime = [i for i in range(m, n + 1) if arr[i]]

if prime:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)