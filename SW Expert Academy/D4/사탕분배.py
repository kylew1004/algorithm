# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX8BB5d6T7gDFARO&categoryId=AX8BB5d6T7gDFARO&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

import sys

input = sys.stdin.readline

def result(a, b, k):
    if a == b:
        return a
        
    for _ in range(k):
        tmp = a if a < b else b
        a = a - tmp if tmp < a else a * 2
        b = b - tmp if tmp < b else b * 2
        print(a, b)
    return min(a , b)
    
N = int(input())
ans = []

for _ in range(N):
    numbers = list(map(int, input().split()))
    ans.append(result(numbers[0], numbers[1], numbers[2]))

for i in range(N):
    print(f"#{i+1} {ans[i]}")