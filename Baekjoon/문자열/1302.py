# https://www.acmicpc.net/problem/1302

import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n):
    title = input()
    dic[title] = dic.get(title, 0) + 1

arr = []
best = max(dic.values())

for book in dic:
    if best == dic[book]:
        arr.append(book)

arr.sort()
print(arr[0])
