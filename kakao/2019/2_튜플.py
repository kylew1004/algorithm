# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def changeToArray(s):
    s = list(s.split("},"))

    for i in range(len(s)):
        s[i] = s[i].replace("{", "")
        s[i] = s[i].replace("}", "")
        s[i] = list(map(int, s[i].split(",")))
    s.sort(key = len)
    return s


def solution(s):
    answer = []

    s = changeToArray(s)

    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] not in answer:
                answer.append(s[i][j])

    return answer
