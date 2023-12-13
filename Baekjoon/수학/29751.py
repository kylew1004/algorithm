# https://www.acmicpc.net/problem/29751

import sys
input = sys.stdin.readline

w, h = map(int, input().split())

print(round(w * h / 2, 1))