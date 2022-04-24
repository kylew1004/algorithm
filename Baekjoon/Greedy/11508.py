# https://www.acmicpc.net/problem/11508

import sys
input = sys.stdin.readline

n = int(input())
arr = []
new_arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse = True)

for i in range(len(arr)):
    if (i + 1) % 3 == 0 :
        continue
    else:
        new_arr.append(arr[i]) 

print(sum(new_arr))