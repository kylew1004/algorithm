# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    id = {}
    index = len(record)
    result = []
    
    for i in reversed(range(index)):
        r = record[i].split()
        if r[0] == "Change" or r[0] == "Enter":
            if r[1] not in id:
                id[r[1]] = id.get(r[1], []) + [r[2]]

    for i in range(index):
        r = record[i].split()
        if r[0] == "Enter":
            result.append(''.join(id[r[1]]) + "님이 들어왔습니다.")
        elif r[0] == "Leave":
            result.append(''.join(id[r[1]]) + "님이 나갔습니다.")
    
    return result
