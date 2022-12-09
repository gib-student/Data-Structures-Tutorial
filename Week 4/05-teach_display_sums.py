"""
CSE212 
(c) BYU-Idaho
05-Teach - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def display_sums(numbers):
    """
    Display pairs of numbers (no duplicates should be displayed) that sum to 
    10 using a set in O(n) time.  We are assuming that there are no duplicates 
    in the list.
    """
    # We will have two lists: possibles and pairs. Possibles will contain
    # unpaired numbers we can search for possible pairs in; when a pair is found, 
    # they will be combined to form a two-value pair list and inserted in pairs.
    possibles   = []
    pairs       = []
    for num in numbers:
        addend = 10 - num
        if addend in possibles:
            pair = [num, addend]
            pairs.append(pair)
            possibles.remove(addend)
        else:
            possibles.append(num)

    # Display the numbers
    for pair in pairs:
        print(f"{pair[0]} {pair[1]}")

display_sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  
"""
Should show something like (order does not matter):
6 4
7 3
8 2
9 1 
"""
print("===========")
display_sums([-20, -15, -10, -5, 0, 5, 10, 15, 20]) 
"""
Should show something like (order does not matter):
10 0
15 -5
20 -10
"""
print("===========")
display_sums([5, 11, 2, -4, 6, 8, -1])
"""
Should show something like (order does not matter):
8 2
-1 11
"""
