# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations
from math import sqrt

def check_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    for arr in combinations(nums, 3):
        total = sum(arr)
        if check_prime(total):
            answer += 1

    return answer