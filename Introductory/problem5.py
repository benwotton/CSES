"""Introductory | Permutations | Problem 5"""

n = int(input())
if n == 1:
    print("1")
elif n < 4:
    print("NO SOLUTION")
else:
    odds = [str(i) for i in range(1, n+1, 2)]
    evens = [str(i) for i in range(2, n+1, 2)]
    print(" ".join(evens + odds))