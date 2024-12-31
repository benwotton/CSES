"""Introductory | Two Sets | Problem 8"""

n = int(input())
total = n*(n+1)//2
if total % 2 == 0:
    print("YES")
    partial_sum = total // 2
    set1 = set()
    for i in range(n, 0, -1):
        if partial_sum - i >= 0:
            set1.add(i)
            partial_sum -= i

        if partial_sum == 0:
            break

    set2 = set()
    for i in range(1, n+1):
        if i not in set1:
            set2.add(i)

    print(len(set1))
    print(" ".join(map(str, set1)))
    print(len(set2))
    print(" ".join(map(str, set2)))
else:
    print("NO")