# https://www.acmicpc.net/problem/1924

import sys
input = sys.stdin.readline

x, y = map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = [0] + days
day = 0

for i in range(1, x):
    day += days[i]
    
day += y
day %= 7

if day == 0:
    print("SUN")
elif day == 1:
    print("MON")
elif day == 2:
    print("TUE")
elif day == 3:
    print("WED")
elif day == 4:
    print("THU")
elif day == 5:
    print("FRI")
else:
    print("SAT")
