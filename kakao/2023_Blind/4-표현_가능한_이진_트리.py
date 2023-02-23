# https://school.programmers.co.kr/learn/courses/30/lessons/150367

'''
유튜브 풀이참조 => https://www.youtube.com/watch?v=nZH8UMudhwA

포화 이진트리는 모든 노드가 2개의 자식 노드를 가지고 있는 트리를 말한다.
조건문에 포화이진트리인지 검사한 후 아닐 경우 이진수의 길이가 2 ** n - 1이 되도록 0을 채워준다.
그 후 dfs를 통해 왼쪽 자식 노드와 오른쪽 자식 노드를 검사한다.

이진 트리 문제가 많이 낯설어서 시간을 잡아먹다가 결국 풀이를 참조했다.
사실 이 문제는 트리구조라기 보다는 구현에 초점이 맞춰진 문제였다.
문제를 볼 때 낯선 유형을 접하더라도 쫄지 않는 습관을 들이자!
'''

def dfs(b, i, depth):
    if depth == 0:
        return 1
    elif b[i] == '0':
        if b[i - depth] == '1' or b[i + depth] == '1':
            return 0

    left = dfs(b, i - depth, depth // 2)
    right = dfs(b, i + depth, depth // 2)

    return 1 if left and right else 0


def solution(numbers):
    answer = []

    for number in numbers:
        number = bin(number)[2:]
        length = bin(len(number) + 1)[2:]
        if '1' in str(length[1:]):
            new_length = int('0b1' + '0' * len(length), 2) - int('0b' + length, 2)
            number = '0' * new_length + number

        result = dfs(number, len(number) // 2, (len(number) + 1) // 4)
        answer.append(result)

    return answer


print(solution(	[7, 42, 5]))
