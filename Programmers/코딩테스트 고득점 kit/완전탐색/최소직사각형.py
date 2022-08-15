# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    length = len(sizes)
    width = 0
    height = 0
    for i in range(length):
        sizes[i].sort()
        if width < sizes[i][0]:
            width = sizes[i][0]
        if height < sizes[i][1]:
            height = sizes[i][1]

    answer = width * height

    return answer