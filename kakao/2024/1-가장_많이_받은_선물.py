# https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    gift_dict = {friend: [0, 0] for friend in friends} # 선물을 준 횟수, 받은 횟수
    gift_given = {f: {} for f in friends}

    for gift in gifts:
        giver, receiver = gift.split()
        gift_dict[giver][0] += 1
        gift_dict[receiver][1] += 1

        if receiver in gift_given[giver]:
            gift_given[giver][receiver] += 1
        else:
            gift_given[giver][receiver] = 1

    next_month_gifts = {friend: 0 for friend in friends} # 다음 달에 받을 선물 수

    for giver in friends:
        for receiver in friends:
            if giver != receiver:
                if receiver in gift_given[giver] and gift_given[giver][receiver] > gift_given[receiver].get(giver, 0):
                    next_month_gifts[giver] += 1
                elif gift_given[giver].get(receiver, 0) == gift_given[receiver].get(giver, 0):
                    giver_index = gift_dict[giver][0] - gift_dict[giver][1]
                    receiver_index = gift_dict[receiver][0] - gift_dict[receiver][1]
                    if giver_index > receiver_index:
                        next_month_gifts[giver] += 1

    max_gifts = max(next_month_gifts.values()) # 가장 많은 선물을 받는 사람의 선물 수
    
    return max_gifts

print("Case 1")
print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
print("Case 2")
print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
print("Case 3")
print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]))