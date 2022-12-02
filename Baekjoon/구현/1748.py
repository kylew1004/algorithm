# https://www.acmicpc.net/problem/1748

n = input()
cnt = 0

for i in range(1, len(n)):
    cnt += 9 * 10 ** (i - 1) * i

cnt += (int(n) - 10 ** (len(n) - 1) + 1) * len(n)
print(cnt)
