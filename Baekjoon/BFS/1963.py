# https://www.acmicpc.net/problem/1963

from collections import deque

def get_prime_numbers():
    prime = [True] * 10000
    prime[0], prime[1] = False, False
    
    for i in range(2, 10000):
        if prime[i] == True:
            j = 2
            while i * j < 10000:
                prime[i * j] = False
                j += 1

    return prime


def bfs(start, target):
    queue = deque()
    queue.append([start, 0])
    visited = [False] * 10000
    visited[start] = True
    
    while queue:
        current, cnt = queue.popleft()

        if current == target:
            return cnt
        current = str(current)
        for i in range(4):
            for j in range(10):
                tmp = int(current[:i] + str(j) + current[i+1:])     # Index 벗어나도 출력안하면 연산은 됨. (이게 되네...)
                if not visited[tmp] and prime_nums[tmp] and tmp >= 1000:
                    visited[tmp] = True
                    queue.append([tmp, cnt + 1])

    return None


t = int(input())
prime_nums = get_prime_numbers()
answer = []

for _ in range(t):
    start, target = map(int, input().split())
    answer.append(bfs(start, target))

for x in answer:
    if x == None:
        print("Impossible")
    else:
        print(x)
