# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(idx, q) for idx, q in enumerate(priorities)])
    find = queue[location][0]

    while queue:
        idx, q = queue.popleft()
        check = 1

        for i, p in queue:
            if p > q:
                queue.append((idx, q))
                check = 0
                break
        if check:
            answer += 1
            if idx == find:
                break

    return answer