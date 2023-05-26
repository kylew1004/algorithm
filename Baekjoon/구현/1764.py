# https://www.acmicpc.net/problem/1764
# 5분정도는 문제가 뭔소린가 했더니 ㅈㄴ 웃기네

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = set(input().rstrip() for _ in range(n))
b = set(input().rstrip() for _ in range(m))
    
c = sorted(list(a & b))

print(len(c))
for i in c:
    print(i)