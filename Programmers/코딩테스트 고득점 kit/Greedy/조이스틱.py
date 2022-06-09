# https://programmers.co.kr/learn/courses/30/lessons/42860

# 🎃주의🎃 절대 쉬운 문제가 아님!!!! 
def solution(name):
    answer = 0
    n = len(name)

    def change_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += change_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer