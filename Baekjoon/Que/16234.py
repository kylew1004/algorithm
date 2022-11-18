# https://www.acmicpc.net/problem/2161

n = int(input())
card = list(range(1, n + 1))

i = 0
while card:
    if i % 2:
        card.append(card.pop(0))
    else:
        print(card.pop(0), end = ' ')
    i += 1