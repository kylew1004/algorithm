# https://www.acmicpc.net/problem/1461

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
books = list(map(int, input().rstrip().split()))
left, right = [], []

for i in range(len(books)):
    if books[i] > 0:
        right.append(books[i])
    elif books[i] < 0:
        left.append(books[i])

left.sort()
right.sort(reverse=True)

max_value = 0
for book in books:
    if abs(max_value) < abs(book):
        max_value = book

cnt = []
for i in range(0, len(left), m):
    if left[i] != max_value:
        cnt.append(abs(left[i]))
for i in range(0, len(right), m):
    if right[i] != max_value:
        cnt.append(right[i])

answer = abs(max_value)
for num in cnt:
    answer += 2 * num

print(answer)
