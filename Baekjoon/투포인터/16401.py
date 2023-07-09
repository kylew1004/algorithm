# https://www.acmicpc.net/problem/16401

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

left = 1
right = max(snacks)
answer = 0

while left <= right:
    mid = (left + right) // 2
    total = 0

    for snack in snacks:
        total += snack // mid

    if total >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)