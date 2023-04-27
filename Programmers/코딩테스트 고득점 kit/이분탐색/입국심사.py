# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        cnt = 0

        for time in times:
            cnt += mid // time

        if cnt >= n:
            answer = mid
            right = mid - 1
        elif cnt < n:
            left = mid + 1

    return answer