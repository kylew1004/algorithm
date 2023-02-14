# https://school.programmers.co.kr/learn/courses/30/lessons/150368

# 노가다 끝에 풀이를 참조...ㅠㅠ
# 처음에 저 코드와 같은 아이디어로 생각함. 시간복잡도를 고려할 때 최대 연산수가 16384 * 100 * 7 = 11,468,800 (16384는 이모티콘과 할인율의 중복조합)
# 완전탐색이 가능하다고 판단해서 설계를 하려했지만 자료구조를 만드는데 애를 먹어서 코드를 참조하였다.
# zip을 활용하여 데이터를 묶어 탐색하는 것이 개꿀인 것 같다. 반드시 써먹도록 하자!!!

from itertools import product

def solution(users, emoticons):
    answer = [0, 0]

    for discount in product([10, 20, 30, 40], repeat = len(emoticons)):
        result = [0, 0]   # 회원수, 매출액
        for term, limit in users:
            total = 0
            for d, e in zip(discount, emoticons):
                if d >= term:
                    total += e * (1 - (d / 100))
            if total >= limit:
                result[0] += 1
            else:
                result[1] += total
        answer = max(answer, result)

    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))