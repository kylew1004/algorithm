# https://www.acmicpc.net/problem/16968

s = input()

answer = 1
d = 10
c = 26
idx = 0

while idx < len(s):
    if s[idx] == 'c':
        answer *= c
        d = 10
        c = 25
    else:
        answer *= d
        c = 26
        d = 9
    idx += 1

print(answer)