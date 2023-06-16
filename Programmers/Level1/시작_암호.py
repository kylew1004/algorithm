# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ""

    for letter in s:
        if letter == " ":
            answer += ' '
        elif ord(letter) < 97:
            answer += chr((ord(letter) - 65 + n) % 26 + 65)
        else:
            answer += chr((ord(letter) - 97 + n) % 26 + 97)

    return answer