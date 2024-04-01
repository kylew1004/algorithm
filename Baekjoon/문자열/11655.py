# https://www.acmicpc.net/problem/11655

import sys
input = sys.stdin.readline

s = input().rstrip()
result = []

for c in s:
    if c.islower():
        result.append(chr((ord(c) - ord('a') + 13) % 26 + ord('a')))
    elif c.isupper():
        result.append(chr((ord(c) - ord('A') + 13) % 26 + ord('A')))
    else:
        result.append(c)
        
print("".join(result))