# https://www.acmicpc.net/problem/2003

n, m = map(int, input().split())
a = list(map(int, input().split()))
start, end = 0, 0
cnt = 0

while start <= end and end <= n:
    result = sum(a[start:end])
    if result == m:
        cnt += 1
        start += 1
        end += 1
        continue
    if result <= m:
        end += 1
        continue
    if result > m and start < end:
        start += 1
        continue

print(cnt)