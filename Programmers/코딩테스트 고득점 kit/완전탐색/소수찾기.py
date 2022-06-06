# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

from itertools import permutations

def is_prime_number(x) :
    if x < 2:
        return False
    if x % 2 == 0 and x != 2:
        return False

    i = 3
    while i*i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

def solution(numbers):
    answer = 0
    num = []

    for i in range(1, len(numbers)+1):
        num.append(list(set(map(''.join, permutations(numbers, i)))))
    
    arr = list(set(map(int, sum(num, [])))) # sum을 이용해 이중리스트를 일차원리스트로 변경
    for n in arr:
        if is_prime_number(n) == True:
            answer += 1
    return answer

numbers = "121"
print(solution(numbers))