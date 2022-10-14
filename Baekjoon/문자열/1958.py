# https://www.acmicpc.net/problem/9935

string = input()
bomb = input()

arr = []
last = bomb[-1]
length = len(bomb)

for s in string:
    arr.append(s)
    if s == last and ''.join(arr[-length:]) == bomb:
        del arr[-length:]

answer = ''.join(arr)

if answer == '':
    print("FRULA")
else:
    print(answer)
