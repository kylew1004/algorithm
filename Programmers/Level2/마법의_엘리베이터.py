# https://school.programmers.co.kr/learn/courses/30/lessons/148653
# (155, 154) 테케 (199, 999), 64 같은 테케에서 걸림;;
# 약간 얻어맞추기 식으로 풀었는데 보완이 필요하다.

def solution(storey):
    answer = 0
    storey = str(storey)
    if int(storey) > 10:
        while int(storey) < 10:
            if int(storey) > 55 * (10 ** (len(storey) - 2)):
                answer += 1
                storey = str(abs(int(storey) - (10 ** len(storey))))
            else:
                answer += int(storey[0])
                storey = storey[1:]
    if int(storey) <= 5:
        answer += int(storey)
    else:
        answer += 10 - int(storey) + 1

    return answer

print(solution(199))