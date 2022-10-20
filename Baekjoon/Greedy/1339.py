# https://www.acmicpc.net/problem/1339

n = int(input())
word_list = [input() for _ in range(n)]
word_dict = {}

for word in word_list:
    power = len(word) - 1
    for i in word:
        if i in word_dict:
            word_dict[i] += pow(10, power)
        else:
            word_dict[i] = pow(10, power)
        power -= 1

word_dict = sorted(word_dict.values(), reverse = True)
answer = 0
num = 9

for word in word_dict:
    answer += word * num
    num -= 1

print(answer)
