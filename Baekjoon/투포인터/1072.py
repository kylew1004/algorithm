# https://www.acmicpc.net/problem/1072

import sys
import math

input = sys.stdin.readline

x, y = map(int, input().split())

z = math.floor(100 * y / x)

if z >= 99:
    print(-1)
else:
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2
        if math.floor(100 * (y + mid) / (x + mid)) > z:
            right = mid - 1
        else:
            left = mid + 1

    print(left)