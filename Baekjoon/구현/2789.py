# https://www.acmicpc.net/problem/2789

import sys
input = sys.stdin.readline

word = list(input().rstrip())
cambridge = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

for i in range(len(word)):
    if word[i] in cambridge:
        word[i] = ''

print(''.join(word))