# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    pokemon = {}
    for i in range(len(nums)):
        pokemon[nums[i]] = pokemon.get(nums[i], 0) + 1
    if len(pokemon) >= len(nums) / 2:
        answer = len(nums) // 2
    else:
        answer = len(pokemon)
    return answer