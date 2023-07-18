# https://www.acmicpc.net/problem/1049

import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
min_package = 1000
min_each = 1000

lines = []
for _ in range(m):
    package, each = map(int, input().split())
    min_package = min(min_package, package)
    min_each = min(min_each, each)
    lines.append((min_package, min_each))

if min_package > min_each * 6:
    print(min_each * n)
elif min_package < n % 6 * min_each:
    print((n // 6 + 1) * min_package)
else:
    print((n // 6) * min_package + n % 6 * min_each)