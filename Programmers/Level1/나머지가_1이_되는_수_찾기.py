# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    for i in range(2, n):
        if (n - 1) % i == 0:
            return i