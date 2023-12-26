# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    else:
        if s % n == 0:
            answer = [s // n] * n
        else:
            cnt = s % n
            answer = [s // n] * n
            idx = n - 1

            while cnt:
                answer[idx] += 1
                cnt -= 1
                idx -= 1 if idx >= 0 else n - 1
    
    return answer