# https://www.acmicpc.net/problem/11866

n, k = map(int, input().split())
l = [i + 1 for i in range(n)]
i = k - 1
result = []

while True:
    if len(l) == 1:
        break
    result.append(l.pop(i))
    i = (i + k - 1)%len(l)
result.append(l.pop())

print("<", end = '')
for i in result[: len(result) - 1]:
    print(i, end = ", ")
print(result[-1], end = ">")
