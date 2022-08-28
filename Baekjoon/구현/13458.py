# https://www.acmicpc.net/problem/13458

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for i in a:
    i -= b
    cnt = 1

    if i > 0:
        cnt += i // c
        if i % c != 0:
            cnt += 1
    answer += cnt

print(answer)