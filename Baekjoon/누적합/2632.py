# https://www.acmicpc.net/problem/2632

import sys
input = sys.stdin.readline

def get_prefix_sum(case, arr, length):
    for i in range(length):
        prefix = arr[i]
        case[prefix] = case.get(prefix, 0) + 1
        for j in range(1, length - 1):
            prefix += arr[(i + j) % length]
            case[prefix] = case.get(prefix, 0) + 1
    case[sum(arr)] = 1
    
    return case


size = int(input())
m, n = map(int, input().split())
a = [int(input()) for _ in range(m)]
b = [int(input()) for _ in range(n)]
case_a = {}
case_b = {}
answer = 0

case_a = get_prefix_sum(case_a, a, m)
case_b = get_prefix_sum(case_b, b, n)

for num in case_a:
    if size - num in case_b:
        answer += case_a[num] * case_b[size - num]

answer += case_a.get(size, 0) + case_b.get(size, 0)

print(answer)