# https://www.acmicpc.net/problem/1251

import sys
input = sys.stdin.readline

word = input().rstrip()
result = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = word[:i][::-1]
        b = word[i:j][::-1]
        c = word[j:][::-1]
        result.append(a + b + c)

print(min(result))