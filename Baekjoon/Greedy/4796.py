# https://www.acmicpc.net/problem/4796

import sys
input = sys.stdin.readline

idx = 0

while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    
    answer = ((v // p) * l) + min((v % p), l)

    idx += 1
    print("Case {}: {}".format(idx, answer))