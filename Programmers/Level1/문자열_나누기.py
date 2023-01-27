# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0
    cnt = 0
    i = 0
    while s:
        start = s[0]
        for i in range(len(s)):
            if s[i] == start:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0 or i == len(s) - 1:
                s = s[i + 1:]
                answer += 1
                break

    return answer

print(solution("banana"))