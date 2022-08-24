# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    num = queue1 + queue2
    cnt = sum(num) / 2
    queue1_sum = sum(queue1)
    
    for _ in range(len(num) * 2):
        if queue1_sum < cnt:
            queue1_sum += queue2[0]
            queue1.append(queue2.popleft())
            answer += 1
        elif queue1_sum > cnt:
            queue1_sum -= queue1[0]
            queue2.append(queue1.popleft())
            answer += 1
        else:
            return answer

    return -1
