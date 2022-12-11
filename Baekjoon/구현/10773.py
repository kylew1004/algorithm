# https://www.acmicpc.net/problem/10773

k = int(input())
stack = []

for i in range(k): 
    num = int(input())
    if(num == 0):
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))
