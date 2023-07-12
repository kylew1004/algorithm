# https://www.acmicpc.net/problem/10814

import sys
input = sys.stdin.readline

n = int(input())
members = []

for idx in range(n):
    age, name = input().split()
    members.append((int(age), name, idx))

members.sort(key=lambda x : (x[0], x[2]))

for member in members:
    print(member[0], member[1])