# https://www.acmicpc.net/problem/4948

import sys
input = sys.stdin.readline

def prime_list(n):
    nums = [True] * (2 * n + 1)
    m = int((2 * n) ** 0.5)

    for i in range(2, m + 1):
        if nums[i] == True:
            for j in range(i + i, 2 * n + 1, i):
                nums[j] = False

    return [i for i in range(n + 1, 2 * n + 1) if nums[i] == True]

while True:
    n = int(input())
    if n == 0:
        break
    print(len(prime_list(n)))