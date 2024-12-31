"""Introductory | Bit Strings | Problem 9"""

n = int(input())
total = 1
for i in range(n):
    total = (total * 2) % (10**9 + 7)

print(total)