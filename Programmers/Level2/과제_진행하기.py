# https://school.programmers.co.kr/learn/courses/30/lessons/176962
# 굉장히 어렵게 풀었다. 나중에 복습하자.

def solution(plans):    
    plans = sorted(plans, key = lambda x : x[1])
    new_plans = []
    stack = []

    for subject, start_time, during_time in plans:
        hh, mm = map(int, start_time.split(":"))
        start = hh * 60 + mm
        end = int(during_time)
        new_plans.append([subject, start, end])

    answer = []
    current_time = new_plans[0][1]
    for i in range(len(new_plans) - 1):
        if new_plans[i + 1][1] < current_time + new_plans[i][2]:
            left_time = new_plans[i][2] - (new_plans[i + 1][1] - current_time)
            stack.append([new_plans[i][0], left_time])
            current_time = new_plans[i + 1][1]
        else:
            answer.append(new_plans[i][0])
            current_time = new_plans[i][1] + new_plans[i][2]
            while stack:
                if current_time + stack[-1][1] > new_plans[i + 1][1]:
                    stack[-1][1] = (current_time + stack[-1][1]) - new_plans[i + 1][1]
                    break
                subject, spend = stack.pop()
                answer.append(subject)
                current_time += spend
            current_time = new_plans[i + 1][1]

    answer.append(new_plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
    
    return answer