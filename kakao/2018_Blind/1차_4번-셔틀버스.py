# https://school.programmers.co.kr/learn/courses/30/lessons/17678

"""
처음 문제를 봤을 때, 버스 시간대를 담는 리스트와 그 시간대에 탑승하는 크루들의 도착시간을 담는 리스트를 구성해야 한다고 생각했다.
그 시간은 HHMM 방식으로 최대한 맞춰서 구현하려 했지만 결국 분단위로 다 바꿔서 구현했다.

힘들었던 부분은 버스시간과 탑승자 시간을 비교하여 새로운 리스트에 담는 과정이었다.
전날 풀었던 카카오 이모티콘 할인행사 문제에서도 비슷한 부분에서 고생을 했는데
그 때의 기억을 되살려 zip함수로 크루의 버스탑승시간 리스트를 구현하였다.

여러 개의 리스트를 참조하여 새로운 리스트를 만드는 부분이 취약한데 꾸준한 연습이 필요하다.
"""

def convert_to_HHMM(time):
    HH = str(time // 60)
    MM = str(time % 60)
    if len(HH) < 2:
        HH = "0" + HH
    if len(MM) < 2:
        MM = "0" + MM

    return HH + ":" + MM


def solution(n, t, m, timetable):
    bus_table = [540 + i * t for i in range(0, n)]  # 버스도착시간(분단위)
    crew_table = []                                 # 크루의 도착시간(분단위)
    passengers_table = [[] for _ in range(n)]       # 버스방문시간별 탑승자 도착시간
    
    timetable.sort()
    for time in timetable:
        HH, MM = map(int, time.split(":"))
        crew_table.append(HH * 60 + MM)

    idx = 0
    for bus_time, passengers in zip(bus_table, passengers_table):
        cnt = 0
        while cnt < m and idx < len(timetable) and crew_table[idx] <= bus_time:
            passengers.append(crew_table[idx])
            idx += 1
            cnt += 1

    if len(passengers_table[-1]) < m:           # 버스의 마지막 시간에 자리가 비면
        return (convert_to_HHMM(bus_table[-1]))
    
    return convert_to_HHMM(passengers_table[-1][-1] - 1)
