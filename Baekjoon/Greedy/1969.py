# https://www.acmicpc.net/problem/1969

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(input())
dna = ''
answer = 0

data.sort()

for y in range(m):
    value = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
    for x in range(n):
        value[data[x][y]] += 1
    dna += max(value, key=value.get)
    answer += n - max(value.values())

print(dna)
print(answer)