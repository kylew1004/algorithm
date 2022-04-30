# https://tech.kakao.com/2020/07/01/2020-internship-test/

def solution(numbers, hand):
    answer = ""
    table = [[1, 4, 7, '*'],[2, 5, 8, 0], [3, 6, 9, '#']]
    left = [0, 3]
    right = [2, 3]

    for n in numbers:
        if n in table[0]:
            answer += 'L'
            left = [0, table[0].index(n)]
        elif n in table[2]:
            answer += 'R'
            right = [2, table[2].index(n)]
        else:
            if (1 - left[0]) + abs((left[1] - table[1].index(n))) > (right[0] - 1) + abs((right[1] - table[1].index(n))):
                answer += 'R'
                right = [1, table[1].index(n)]
            elif (1 - left[0]) + abs((left[1] - table[1].index(n))) < (right[0] - 1) + abs((right[1] - table[1].index(n))):
                answer += 'L'
                left = [1, table[1].index(n)]
            else:
                if hand == "left":
                    answer += "L"
                    left = [1, table[1].index(n)]
                else:
                    answer += 'R'
                    right = [1, table[1].index(n)]
    return answer
