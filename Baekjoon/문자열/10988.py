# https://www.acmicpc.net/problem/10988

import sys
input = sys.stdin.readline

word = input().rstrip()
length = len(word)

for i in range(length // 2):
    if word[i] != word[length - i - 1]:
        print(0)
        break
else:
    print(1)
