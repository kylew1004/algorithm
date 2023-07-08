# https://www.acmicpc.net/problem/1940

n = int(input())
m = int(input())
weapons = list(map(int, input().split()))
weapons.sort()
answer = 0
left = 0
right = n - 1

while left < right:
    if weapons[left] + weapons[right] == m:
        answer += 1
        left += 1
    elif weapons[left] + weapons[right] < m:
        left += 1
    else:
        right -= 1

print(answer)