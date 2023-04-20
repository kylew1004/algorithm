# https://school.programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    answer = ''
    answer_time = 0

    def change(code):
        code = code.replace("C#", "c")
        code = code.replace("D#", "d")
        code = code.replace("F#", "f")
        code = code.replace("G#", "g")
        code = code.replace("A#", "a")

        return code

    m = change(m)

    for info in musicinfos:
        start, end, title, code = info.split(",")
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        time = (eh - sh) * 60 + (em - sm)
        code = change(code)
        if len(code) < time:
            code += code * (time // len(code))
        code = code[:time]
        if m in code:
            if answer_time < time:
                answer = title
                answer_time = time

    if answer == '':
        answer = "(None)"

    return answer