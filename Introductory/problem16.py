"""Introductory | Apple Division | Problem 16"""

n = int(input())
p = list(map(int, input().split()))
midpoint = sum(p)/2

subset_totals = []
def backtrack(i, curr_total):
    if i == n:
        if curr_total == midpoint:
            print(0)
            quit()

        subset_totals.append(curr_total)
        return

    backtrack(i+1, curr_total)
    curr_total += p[i]
    backtrack(i+1, curr_total)
    curr_total -= p[i]

backtrack(0, 0)

minimal_difference = abs(midpoint - p[0])
for subset_total in subset_totals:
    if abs(midpoint - subset_total) < minimal_difference:
        minimal_difference = abs(midpoint - subset_total)

print(int(2 * minimal_difference))