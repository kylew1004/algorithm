# https://www.acmicpc.net/problem/1874

n = int(input())
stack = []
answer = []
find = True
now = 1

for _ in range(n):
    num = int(input())
    
    while now <= num:
        stack.append(now)
        answer.append('+')
        now += 1
        
    if stack[-1] == num:
        stack.pop()
        answer.append('-')

    else:
        find = False

if not find:
    print('NO')
else:
    for i in answer :
        print(i)
