# https://www.acmicpc.net/problem/10819

from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
answer = 0

for per in permutations(range(n), n):
    tmp = 0
    for i in range(1, n):
        tmp += abs(arr[per[i]] - arr[per[i-1]])
    answer = max(answer, tmp)

print(answer)
