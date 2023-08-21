# https://www.acmicpc.net/problem/19941

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(input().rstrip())
ans = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(i - k, i + k + 1):
            if 0 <= j < n and arr[j] == 'H':
                ans += 1
                arr[j] = 'X'
                break

print(ans)
