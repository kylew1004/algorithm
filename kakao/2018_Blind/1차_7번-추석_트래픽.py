# https://school.programmers.co.kr/learn/courses/30/lessons/17676
'''
문제에서 날짜는 고정이라는 전제를 주었기 때문에 시간만 계산하면 된다.
다만 시간을 초단위로 계산하게 되면 ms단위를 float로 변환하는 과정에서 0.000009와 같은 이상한 값이 따라붙게된다.

그래서 반드시 모든 단위를 int로 통일시켜야 한다. (이것 때문에 애를 먹음..)
'''

def count(start, end, log):
    cnt = 0
    for s, e in log:
        if s < end and e >= start :
            cnt += 1

    return cnt


def solution(lines):
    answer = 0
    
    log = []
    for line in lines:
        date, start, gen = line.split(" ")
        time = list(start.split(":"))
        gen = gen.rstrip("s")
        end = (3600 * int(time[0]) + 60 * int(time[1]) + float(time[2])) * 1000
        start = end - (float(gen) * 1000) + 1
        log.append([start, end])
    for start, end in log:
        answer = max(answer, count(start, start + 1000, log), count(end, end + 1000, log))
    
    return answer

print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))