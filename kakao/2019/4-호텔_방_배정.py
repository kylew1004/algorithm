# https://school.programmers.co.kr/learn/courses/30/lessons/64063

def solution(k, room_number):   # k는 함정이다. 방개수를 k+1개로 만들면 시간초과가 나서 링크드리스트형태로 방문횟수를 줄여야 한다.
    answer = []
    rooms = {}
    
    for num in room_number:
        start = rooms.get(num, 0)

        if start:
            idx = start
            visited = []
            while True:
                if not rooms.get(idx, 0):
                    rooms[idx] = rooms.get(idx, idx + 1)
                    answer.append(idx)
                    break
                else:
                    idx = rooms[idx]
                    visited.append(idx)
            for i in visited:
                rooms[i] = idx + 1

        else:
            rooms[num] = rooms.get(num, num + 1)
            answer.append(num)

    return answer
