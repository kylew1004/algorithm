# https://www.acmicpc.net/problem/1747

import sys
input = sys.stdin.readline
    
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def isPalindrome(n):
    n = str(n)
    return n == n[::-1]

n = int(input())

while True:
    if isPalindrome(n) and isPrime(n):
        print(n)
        break
    n += 1