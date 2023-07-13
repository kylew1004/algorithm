# https://www.acmicpc.net/problem/2910

n, c = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
hashmap = {}

for i in arr:
    hashmap[i] = hashmap.get(i, 0) + 1

hashmap = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))

for n in hashmap:
    answer += [n] * hashmap[n]

print(' '.join(map(str, answer)))