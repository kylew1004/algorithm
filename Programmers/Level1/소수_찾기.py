# https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0
    
    def isPrime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

    for i in range(2, n + 1):
        if isPrime(i):
            answer += 1

    return answer