# https://school.programmers.co.kr/learn/courses/30/lessons/77484#

def solution(lottos, win_nums):
    top = len(win_nums) + 1
    bottom = top
    
    for l in lottos:
        if l == 0:
            top -= 1
        elif l in win_nums:
            top -= 1
            bottom -= 1
    
    if top >= len(win_nums):
        top -= 1
    if bottom > len(win_nums):
        bottom -= 1

    answer = [top, bottom]
    
    return answer