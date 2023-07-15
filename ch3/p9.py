"""
Brute force: For each number in the sequence, branch to a node where a possible letter from that number is used.
So 269 branches to nodes 'a', 'b', c' (because 2 => abc). From each of those nodes, branch to 3 more nodes (because 6
=> mno). This looks like a tree of height m (where m = length of sequence), with each non-leaf node having 3-4
branches that we must iterate through to all leafs to collect the result strings. We can do this without a tree,
just with recursive funciton calls (DFS). Takes O(4^m) time, O(m) space (max possible call stack height) to fully
recurse through all options, and assuming at the end of each string result we don't store it at all but just yield
a pointer if the string exists in the dictionary (let's assume this is a generator function). Otherwise O(m + nm) space,
because we possibly could have n words with m letters each that need to be stored additionally.

For each dict check, whether dict is an unsorted array of strings (represented as linked lists) or a linked list of
pointers to arrays, single char comparison necesitates checking up to n elements and checking up to m chars of each
element, so worst case O(mn) time. Combined with the outer process, that's O(4^m * nm) time.

In conclusion, brute force can be:
Time: O(4^m * mn)
Space: O(mn)

Improvements:
If the dict is sorted, it could still be checking n elements, m chars. Best case improves though.
If we have a suffix tree for our dict, we can check existence in exactly O(m) time.
If we hash each word (i.e. mapping words to ints), we can check the dict in O(1) time, assuming an even hashing.

We can't improve the outer process from O(4^m) time since we need to check each option, but we can reduce space usage
to O(m) using a generator (essentially deferring the storage process of the result to the calling function), and I think
that's about it.

Can probably also optimize such that if the sequence is longer than anything in the dict, we don't even bother at all.

In conclusion, optimal is probably:
Time: O(4^m) (using hash, or O(4^m * m) using suffix tree)
Space: O(mn) (or generator for O(m))
"""
# from typing import Generator
from english_words import get_english_words_set

from util import asserter

words = get_english_words_set(['web2'])

digit_to_chars = {
    '2': ('a', 'b', 'c'),
    '3': ('d', 'e', 'f'),
    '4': ('g', 'h', 'i'),
    '5': ('j', 'k', 'l'),
    '6': ('m', 'n', 'o'),
    '7': ('p', 'q', 'r', 's'),
    '8': ('t', 'u', 'v'),
    '9': ('w', 'x', 'y', 'z'),
}


def t9(seq: str) -> list[str]:
    res = []

    def go(i: int, acc: str):
        if i == len(seq):
            if acc in words:
                print(acc)
                res.append(acc)
        else:
            for char in digit_to_chars[seq[i]]:
                go(i + 1, acc + char)

    go(0, '')

    return res


asserter(lambda: t9('269'), ['amy', 'any', 'bow', 'boy', 'cow', 'cox', 'coy', 'coz'])
