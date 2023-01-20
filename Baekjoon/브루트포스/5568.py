# https://www.acmicpc.net/problem/5568

from itertools import permutations
import sys
input = sys.stdin.readline

n, k = int(input()), int(input())
cards = [input().rstrip() for _ in range(n)]
answer = set()
for permutation in permutations(cards, k):
    answer.add(''.join(permutation))
    
print(len(answer))
