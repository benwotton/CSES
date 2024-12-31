"""Introductory | Coin Piles | Problem 11"""

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        print("YES")
        continue

    if a == 0 or b == 0 or a > 2 * b or b > 2 * a or ((2*b - a)/3) % 1 != 0:
        print("NO")
    else:
        print("YES")