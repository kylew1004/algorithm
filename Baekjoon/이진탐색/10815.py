# https://www.acmicpc.net/problem/10815

import sys
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
checks = list(map(int, input().split()))

for check in checks:
    start, end = 0, n - 1
    flag = False

    while start <= end:
        mid = (start + end) // 2
        if cards[mid] > check:
            end = mid - 1
        elif cards[mid] < check:
            start = mid + 1
        else:
            flag = True
            break

    print(1 if flag else 0, end=' ')