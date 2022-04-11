# https://www.acmicpc.net/problem/1316

import sys

input = sys.stdin.readline

n = int(input())
ans = n

for i in range(n):
    word = input()
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            pass
        elif word[j] in word[j + 1:]:
            ans -= 1
            break

print(ans)