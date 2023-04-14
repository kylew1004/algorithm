# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]

def solution(n, t, m, p):
    answer = ''
    
    words = ''
    cnt = 0
    length = 0
    
    while cnt < t * m:
        words += convert_notation(cnt, n)
        cnt += 1

    while length != t:
        answer += words[length * m + (p - 1)]
        length += 1
    
    return answer
