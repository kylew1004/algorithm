# https://school.programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    answer = []

    def hanoi(N, start, target, mid, answer):
        if N == 1:
            answer.append([start, target])
        else:
            hanoi(N - 1, start, mid, target, answer)
            answer.append([start, target])
            hanoi(N - 1, mid, target, start, answer)

    hanoi(n, 1, 3, 2, answer)

    return answer