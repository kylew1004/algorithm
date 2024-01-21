# https://school.programmers.co.kr/learn/courses/30/lessons/250137

def solution(bandage, health, attacks):
    hp = health
    prev = 0

    for t, attack in attacks:
        term = (t - 1) - prev
        hp += term * bandage[1] + bandage[2] * (term // bandage[0])
        if hp >= health:
            hp = health
        hp -= attack
        prev = t

        if hp <= 0:
            hp = -1
            break

    return hp