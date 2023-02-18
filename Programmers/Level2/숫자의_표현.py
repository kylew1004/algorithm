# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        cnt = 0
        for j in range(i, n + 1):
            cnt += j
            if cnt == n:
                answer += 1
            elif cnt > n:
                break

    return answer
