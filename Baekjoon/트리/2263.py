# https://www.acmicpc.net/problem/2263

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def pre_order(in_l, in_r, post_l, post_r):
    if in_l > in_r or post_l > post_r:
        return

    root=post_order[post_r]
    print(root, end=" ")

    left = idx[root] - in_l
    right = in_r - idx[root]

    pre_order(in_l, in_l + left - 1, post_l, post_l + left - 1)
    pre_order(in_r - right + 1, in_r, post_r - right, post_r - 1)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

idx = [0] * (n + 1)

for i in range(n):
    idx[in_order[i]] = i

pre_order(0, n - 1, 0, n - 1)