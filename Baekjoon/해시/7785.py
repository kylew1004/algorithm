# https://www.acmicpc.net/problem/7785

import sys
input = sys.stdin.readline

n = int(input())
arr = set()

for _ in range(n):
    name, status = input().split()
    if status == "enter":
        arr.add(name)
    else:
        arr.remove(name)
        
print("\n".join(sorted(arr, reverse=True)))