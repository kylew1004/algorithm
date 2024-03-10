# https://www.acmicpc.net/problem/25206

import sys
input = sys.stdin.readline

major_score = 0
total = 0
dic = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
for _ in range(20):
    subject, score, grade = input().split()
    if grade != "P":
        major_score += float(score) * dic[grade]
        total += float(score)

print(round(major_score / total, 6) if total else "0.00")