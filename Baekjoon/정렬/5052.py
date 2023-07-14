# https://www.acmicpc.net/problem/5052

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    phone = []
    for _ in range(n):
        phone.append(input().rstrip())
    phone.sort()
    flag = True
    for i in range(n - 1):
        if phone[i] == phone[i + 1][:len(phone[i])]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")