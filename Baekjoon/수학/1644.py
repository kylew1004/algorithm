# https://www.acmicpc.net/problem/1644

import sys
input = sys.stdin.readline

n = int(input())
prime = [True] * (n + 1)
prime[0] = prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False

prime = [i for i in range(n + 1) if prime[i]]

answer = 0
left = right = 0
total = 0

while True:
    if total >= n:
        if total == n:
            answer += 1
        total -= prime[left]
        left += 1
    elif right == len(prime):
        break
    else:
        total += prime[right]
        right += 1
        
print(answer)