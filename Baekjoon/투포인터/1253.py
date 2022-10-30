# https://www.acmicpc.net/problem/1253

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

for i, num in enumerate(arr):
    tmp = arr[:i] + arr[i + 1:]
    left, right = 0, len(tmp) - 1
    while left < right:
        if tmp[left] + tmp[right] > num:
            right -= 1
        elif tmp[left] + tmp[right] < num:
            left += 1
        else:
            answer += 1
            break

print(answer)
