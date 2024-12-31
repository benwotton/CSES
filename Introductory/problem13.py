"""Introductory | Gray Code | Problem 13"""

n = int(input())
cycle = "0110"
i = 0
for i in range(0, 2**n):
    for j in range(n-1, -1, -1):
        print(cycle[(i//(2**j))%4], end="")

    print()