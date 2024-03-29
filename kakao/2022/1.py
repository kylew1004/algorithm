# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    result = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    for i in range(len(survey)):
        if choices[i] < 4:
            result[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            result[survey[i][1]] += choices[i] - 4

    if result.get("R") >= result.get("T"):
        answer += "R"
    else:
        answer += "T"
    if result.get("C") >= result.get("F"):
        answer += "C"
    else:
        answer += "F"
    if result.get("J") >= result.get("M"):
        answer += "J"
    else:
        answer += "M"
    if result.get("A") >= result.get("N"):
        answer += "A"
    else:
        answer += "N"

    return answer