# https://www.acmicpc.net/problem/1977

import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

arr = []
for i in range(1, 101):
    if i ** 2 >= m and i **2  <= n:
        arr.append(i ** 2)
        
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
