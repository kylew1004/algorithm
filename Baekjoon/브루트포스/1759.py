# https://www.acmicpc.net/problem/1759

from itertools import combinations

def check(string):
    cnt = 0
    for alpha in string:
        if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u':
            cnt += 1
    return cnt


l, c = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()

for case in combinations(alphabet, l):
    if check(case) >= 1 and (len(case) - check(case)) >= 2:
        print(''.join(case))