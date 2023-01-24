# https://school.programmers.co.kr/learn/courses/30/lessons/150369

# 생각보다 쉽지 않은 문제;; 16-20 테케가 계속 시간초과로 걸린다;;
# while 문 break 조건을 걸기 위해서는 del arr[-1] 같은 방법을 쓰는 것 보다 수거와 배달의 index를 만들어 주는 것이 효율적이다.

def solution(cap, n, deliveries, pickups):
    answer = 0
    index_d = n - 1
    index_p = n - 1

    while index_d > -1 or index_p > -1:
        hold = cap
        visit_d = 0
        visit_c = 0
        while hold and index_d >= 0:
            if not deliveries[index_d]:
                index_d -= 1
            else:
                deliveries[index_d] -= 1
                hold -= 1
                visit_d = max(visit_d, index_d + 1)
        hold = 0
        while hold < cap and index_p >= 0:
            if not pickups[index_p]:
                index_p -= 1
            else:
                pickups[index_p] -= 1
                hold += 1
                visit_c = max(visit_c, index_p + 1)
        answer += (max(visit_d, visit_c)) * 2
    return answer

print(solution(2, 2, [0,0], [0,4]))