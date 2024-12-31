"""Introductory | Two Knights | Problem 7"""

n = int(input())
print(0)
for k in range(2, n+1):
    combinations = (k**2 * (k**2-1)) // 2
    combinations -= (10 + 4*(k-4)) * (k-2) + (4 + 2*(k-4))
    print(combinations)