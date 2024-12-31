"""Introductory | Tower of Hanoi | Problem 14"""

n = int(input())

def solve(n, dest, src):
    if n == 1:
        print(src, dest)
        return

    new_dest = 6 - src - dest
    solve(n-1, new_dest, src)
    print(src, dest)
    solve(n-1, dest, new_dest)

print(2**n-1)
result = solve(n, 3, 1)