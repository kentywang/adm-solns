from util import asserter

"""
Anagrams have same total letter count and counts for each letter.
So have an 26-element array of ints to store letter counts.

Time: O(min(x,y)) where x = length of 1st string, y = length of 2nd string
Space: O(1) (just need two fixed-size arrays)   
"""


def count(word: str) -> list[int]:
    arr = [0] * 26

    for char in word:
        arr[ord(char) - 97] += 1

    return arr


def anagram(x: str, y: str) -> bool:
    if len(x) != len(y):
        return False

    return count(x) == count(y)


asserter(lambda: anagram('silent', 'listen'), True)
asserter(lambda: anagram('incest', 'insect'), True)
asserter(lambda: anagram('baa', 'bab'), False)
asserter(lambda: anagram('aab', 'ab'), False)
