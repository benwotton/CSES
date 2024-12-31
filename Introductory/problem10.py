"""Introductory | Trailing Zeros | Problem 10"""

n = int(input())
count = 0
i = 1
while True:
    if n // (5**i) == 0:
        break

    count += n // (5**i)
    i += 1

print(count)