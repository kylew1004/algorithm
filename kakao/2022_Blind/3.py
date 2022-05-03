# https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

import math

def convert(time):
    hh, mm = time.split(':')
    return int(hh) * 60 + int(mm)

def solution(fees, records):
    intime = {}
    result = {}
    for record in records:
        time, num, inout = record.split()
        if inout == "IN":
            intime[num] = convert(time)
            if num not in result:
                result[num] = 0
        else:
            result[num] += convert(time) - intime[num]
            del intime[num]
    
    for key, val in intime.items():
        result[key] += 23 * 60 + 59 - val

    answer = []
    for key, val in sorted(result.items()):
        if val <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((val - fees[0]) / fees[2]) * fees[3])
    return answer