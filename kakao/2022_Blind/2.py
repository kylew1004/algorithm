# https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

def isPrime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution(n, k):
    arr = []
    answer = []
    while n != 0:
        arr.append(n % k)
        n = n // k
    arr.reverse()
    arr = ''.join(map(str, arr))

    for i in arr.split('0'):
        if i and isPrime(int(i)):
                answer.append(int(i))

    return len(answer)
