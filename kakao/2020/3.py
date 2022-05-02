# https://tech.kakao.com/2020/07/01/2020-internship-test/

def solution(gems):
    N = len(gems)
    n_gems = set(gems)                                 #   보석 종류
    get_gems = {gems[0]:1, }                           #   현재 가진 보석종류
    start, end = 0, 0
    answer = [0, len(gems)]

    while start < N and end < N:
        if len(get_gems) < len(n_gems):
            end += 1
            if end == N:
                break
            get_gems[gems[end]] = get_gems.get(gems[end], 0) + 1
        else:
            if (end - start + 1) < answer[1] - answer[0] + 1:
                answer = [start, end]
            if get_gems[gems[start]] == 1:
                del get_gems[gems[start]]
            else:
                get_gems[gems[start]] -= 1
            start += 1

    answer = [answer[0]]
    return answer