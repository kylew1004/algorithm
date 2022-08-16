# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product

def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    arrays = []
    
    for i in range(1, 6):
        for cwr in product(vowels, repeat = i):
            arrays.append(cwr)
    arrays.sort()

    for i in range(len(arrays)):
        if ''.join(arrays[i]) == word:
            answer = i + 1
            break

    return answer