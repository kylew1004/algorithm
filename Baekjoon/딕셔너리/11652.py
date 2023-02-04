# https://www.acmicpc.net/problem/11652

import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n) :
    card = int(input())
    if card in dic :
        dic[card] += 1
    else :
        dic[card] = 1

answer = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
print(answer[0][0])
