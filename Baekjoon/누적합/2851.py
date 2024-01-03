# https://www.acmicpc.net/problem/2851

import sys
input = sys.stdin.readline

mushrooms = [int(input()) for _ in range(10)]
sum = 0
for i in range(10):
    sum += mushrooms[i]
    if sum >= 100:
        if sum - 100 <= 100 - (sum - mushrooms[i]):
            print(sum)
        else:
            print(sum - mushrooms[i])
        break
else:
    print(sum)