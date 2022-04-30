# https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

def check(num):
    if num == 2 or num == 3:
        return True
    if num < 2:
        return False
    
    i = 2
    while i <= num / 2:
        if num % i == 0:
            return False
        i += 1
    return True

def solution(n, k):
    arr = []
    answer = []
    while n != 0:
        arr.append(n % k)
        n = n // k
    arr.reverse()

    i = 0
    tmp = []
    while i < len(arr):
        if arr[i] == 0:
            if check(int(''.join(map(str, tmp)))):
                answer.append(int(''.join(map(str, tmp))))
            tmp = []
        else:
            tmp.append(arr[i])
        i += 1
        if i == len(arr):
            if check(int(''.join(map(str, tmp)))):
                answer.append(int(''.join(map(str, tmp))))
                print(answer)

    return len(answer)

solution(437674, 3)