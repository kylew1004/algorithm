# https://www.acmicpc.net/problem/10867

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums = sorted(list(set(nums)))

print(' '.join(map(str, nums)))