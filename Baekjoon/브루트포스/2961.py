# https://www.acmicpc.net/problem/2961

from itertools import combinations
    
n = int(input())
products = [list(map(int, input().split())) for _ in range(n)]

def get_sour_bitter(comb):
    sour = 1
    bitter = 0

    for s, b in comb:
        sour *= s
        bitter += b
    
    return sour, bitter

sour = 0
bitter = 0

for i in range(1, n + 1):
    for comb in combinations(products, i):
        s, b = get_sour_bitter(comb)
        if sour == 0 or (abs(s - b) < abs(sour - bitter)):
            sour = s
            bitter = b

print(abs(sour - bitter))