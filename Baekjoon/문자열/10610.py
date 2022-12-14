# https://www.acmicpc.net/problem/10610

n = list(input())
answer = -1

max_num = sorted(n, reverse = True)
max_num = int(''.join(max_num))

if max_num % 30 == 0:
    answer = max_num

print(answer)
