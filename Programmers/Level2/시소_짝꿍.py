# https://school.programmers.co.kr/learn/courses/30/lessons/152996
# 참조 코드 : https://prod.velog.io/@8804who/프로그래머스시소-짝꿍
# 시간초과가 계속 발생하여 코드를 참조;; 공부가 더 필요하다.

def solution(weights):
    answer = 0
    arr = [0] * 1001
    for i in weights:
        arr[i] += 1

    for i in range(100, 1001):
        for j in [1, 3 / 2, 2, 4 / 3]:
            num = int(i * j)
            if num != i * j:
                continue
            if num < 1001:
                if i == num:
                    if arr[i] > 1:
                        answer += (arr[i] * (arr[i] - 1)) // 2
                else:
                    answer += arr[i] * arr[num]
    
    return answer
