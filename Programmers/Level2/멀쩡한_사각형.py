# https://school.programmers.co.kr/learn/courses/30/lessons/62048

def solution(w, h):
    def gcd(a, b):  # 유클리드 호제법
        while b:
            a, b = b, a % b
        return a


    x = gcd(w, h)
    answer = w * h - (w / x + h / x - 1) * x
    
    return answer