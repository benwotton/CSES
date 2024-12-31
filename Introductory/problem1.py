"""Introductory | Weird Algorithm | Problem 1"""

n = int(input())
while True:
    if n == 1: break
    print(n, end=" ")
    n = n//2 if n % 2 == 0 else 3*n+1

print(1)