# https://www.acmicpc.net/problem/10039

import sys
input = sys.stdin.readline

scores = [int(input()) for _ in range(5)]
print(sum([score if score >= 40 else 40 for score in scores]) // 5)