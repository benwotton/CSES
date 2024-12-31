"""Introductory | Creating Strings | Problem 15"""

permutations = set()
def permute(items, i):
    if i == len(items)-1:
        permutations.add("".join(items))

    for j in range(i, len(string)):
        if j > i and items[i] == items[j]:
            continue

        new = items.copy()
        new[i], new[j] = new[j], new[i]
        permute(new, i+1)

string = input()
permute(list(string), 0)
print(len(permutations))
for permutation in sorted(permutations):
    print(permutation)