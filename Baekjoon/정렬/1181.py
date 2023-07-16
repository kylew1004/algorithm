# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    word = input().rstrip()
    words.append((len(word), word))

words = list(set(words))
words = sorted(words, key = lambda x: (x[0], x[1]))

for word in words:
    print(word[1])