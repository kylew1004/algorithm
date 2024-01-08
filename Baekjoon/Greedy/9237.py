# https://www.acmicpc.net/problem/9237

import sys
input = sys.stdin.readline

n = int(input())
tree = sorted(list(map(int, input().split())), reverse = True)

for i in range(n):
    tree[i] += i + 1

print(max(tree) + 1)