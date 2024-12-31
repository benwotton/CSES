"""Introductory | Increasing Array | Problem 4"""

n = int(input())
x = list(map(int, input().split()))
total = 0
for i in range(1, len(x)):
    if x[i] < x[i-1]:
        total += x[i-1] - x[i]
        x[i] = x[i-1]

print(total)