"""Introductory | Repetitions | Problem 3"""

n = input()
char = n[0]
curr, best = 0, 0
for i in range(len(n)):
    if char == n[i]:
        curr += 1
    else:
        best = max(best, curr)
        char = n[i]
        curr = 1

print(max(best, curr))