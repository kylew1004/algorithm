# https://atcoder.jp/contests/abc333/tasks/abc333_c

n = int(input().strip())

sums = set()
for i in range(1, 13):
    for j in range(i, 13):
        for k in range(j, 13):
            sums.add(int('1' * i) + int('1' * j) + int('1' * k))

sorted_sums = sorted(list(sums))
print(sorted_sums[n - 1])