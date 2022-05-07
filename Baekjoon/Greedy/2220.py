# https://www.acmicpc.net/problem/2220

import sys
input = sys.stdin.readline

n = int(input())
heap = [0, 1]

def swap(arr, x, y):
    tmp = arr[x]
    arr[x] = arr[y]
    arr[y] = tmp

for i in range(2, n + 1):
    heap.append(i)
    swap(heap, i, i - 1)
    j = i - 1
    while j != 1:
        swap(heap, j, j // 2)
        j = j // 2

print(' '.join(map(str, heap[1:])))