# https://www.acmicpc.net/problem/16440

n = int(input())
cake = list(input())
s = 0

for i in range(n // 2):
    if cake[i] == 's':
        s += 1

if s == n // 4:
    print(1)
    print(n // 2)

else:
    for i in range(n // 2):
        if cake[i] == 's':
            s -= 1
        if cake[i + n // 2] == 's':
            s += 1
        if s == n // 4:
            print(2)
            print(i + 1, (i + 1) + n // 2)
            break
