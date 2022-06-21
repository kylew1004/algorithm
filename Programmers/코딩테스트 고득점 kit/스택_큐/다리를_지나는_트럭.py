# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weight = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])

    while truck_weights or bridge_weight:
        bridge_weight -= bridge.popleft()
        if truck_weights and bridge_weight + truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft())
            bridge_weight += bridge[-1]
        else:
            bridge.append(0)
        answer += 1

    return answer