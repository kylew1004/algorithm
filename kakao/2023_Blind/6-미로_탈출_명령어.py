# https://school.programmers.co.kr/learn/courses/30/lessons/150365


# 코드참조: https://github.com/Juniork725/coding_test/blob/main/%EB%82%9C%EC%9D%B4%EB%8F%843/%EB%AF%B8%EB%A1%9C%20%ED%83%88%EC%B6%9C%20%EB%AA%85%EB%A0%B9%EC%96%B4.md
# 처음에 내가 생각한 풀이와 비슷하지만 나는 dddduuu를 많이 넣어서 하는 식으로 했지만 조금 잘못된 풀이였다.
# d를 최대한 넣고 l을 넣고 rl을 반복하다가 마지막에 u을 넣는게 최소인데 이를 고려하지 못했다.

def solution(n, m, x, y, r, c, k):
    answer = ''
    moves = {'d' : 0, 'l' : 0, 'r' : 0, 'u' : 0}

    k -= abs(r - x) + abs(c - y)
    if k < 0 or k % 2 != 0:
        return "impossible"

    if x > r:
        moves['u'] += x - r
    else:
        moves['d'] += r - x
    if y > c:
        moves['l'] += y - c
    else:
        moves['r'] += c - y

    answer += 'd' * moves['d']
    d = min(k // 2, n - (x + moves['d']))
    answer += 'd' * d
    moves['u'] += d
    k -= 2 * d

    answer += 'l' * moves['l']
    l = min(k // 2, y - moves['l'] - 1)
    answer += 'l' * l
    moves['r'] += l
    k -= 2 * l

    answer += 'rl' * (k // 2)
    answer += 'r' * moves['r']
    answer += 'u' * moves['u']

    return answer
