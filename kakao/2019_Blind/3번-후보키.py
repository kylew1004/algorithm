# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    row,col = len(relation), len(relation[0])  
    candidates = []
    unique = []

    for i in range(1, col + 1): 
        candidates.extend(combinations(range(col), i))
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == row:
            unique.append(keys)
    answer = set(unique)

    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):    # intersection => 교집합제거
                answer.discard(unique[j])          # discard 와 remove는 같은 기능이지만 discard는 요소가 없어도 실행가능
    return len(answer)
