"""Introductory | Palindrome Reorder | Problem 12"""

def get_letter_count(string):
    letters = {}
    for char in string:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    return letters

string = input()
letters = get_letter_count(string)
if len(string) % 2 == 0:
    for count in letters.values():
        if count % 2 == 1:
            print("NO SOLUTION")
            quit()

elif len(string) % 2 == 1:
    seen_odd = False
    for count in letters.values():
        if count % 2 == 1:
            if seen_odd == True:
                print("NO SOLUTION")
                quit()

            seen_odd = True

start = ""
middle = ""
end = ""
for letter, count in letters.items():
    if count % 2 == 0:
        start += letter * (count//2)
        end += letter * (count//2)

    elif count % 2 == 1:
        start += letter * ((count-1)//2)
        end += letter * ((count-1)//2)
        middle += letter

print(start + middle + end[::-1])