# https://www.acmicpc.net/problem/2470

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
tmp_start, tmp_end = 0, n - 1
start, end = tmp_start, tmp_end
answer = arr[0] + arr[n - 1]

while tmp_start < tmp_end:
    result = arr[tmp_start] + arr[tmp_end]
    if abs(result) <= abs(answer):
        answer = result
        start, end = tmp_start, tmp_end
        if answer == 0:
            break
    if result < 0:
        tmp_start += 1
    else:
        tmp_end -= 1

print(arr[start], arr[end])