# https://tech.kakao.com/2021/07/08/2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-for-tech-developers-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%B4%EC%84%A4/

import sys
input = sys.stdin.readline

n = list(map(str, input()))
numbers_1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
res = []

for i in range(len(n)):
    if n[i] in numbers_2:
        res.append(n[i])
    else :
        j = i
        tmp = []
        while (''.join(tmp) not in numbers_1 and len(tmp) != 5 and j != len(n)):
           tmp.append(n[j].lower())
           j += 1
        if ''.join(tmp) in numbers_1:
            index = numbers_1.index(''.join(tmp))
            res.append(numbers_2[index])

print(''.join(res))