"""Introductory | Number Spiral | Problem 6"""

t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    highest = max(y, x)
    if highest % 2 == 0:
        print((highest - 1)**2 + y - x + highest)
    else:
        print((highest - 1)**2 + x - y + highest)