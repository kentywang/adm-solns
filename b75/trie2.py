from dataclasses import dataclass, field
from typing import ForwardRef, Optional

from util import asserter


@dataclass
class Node:
    terminating: bool = False
    children: dict[str, Optional[ForwardRef('Node')]] = field(default_factory=dict)


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Same as trie1.py
        """
        curr = self.root
        for c in word:
            if c in curr.children:
                # exists, so traverse to it and do next char
                curr = curr.children[c]
            else:
                curr.children[c] = Node()
                curr = curr.children[c]
        curr.terminating = True

    def search(self, word: str) -> bool:
        """
        Time: Depends on number and kind of insertions. E.g. if there are 5 letters per node, then O(5^w)
        Space: O(1)
        """

        def dfs(i, curr):
            for j in range(i, len(word)):
                if word[j] == '.':
                    # Wildcard, so branch to each child, upping the index so we check the next letter in the word.
                    # If no children, this evaluates to False
                    return any(dfs(j + 1, curr.children[c]) for c in curr.children)
                if word[j] in curr.children:
                    curr = curr.children[word[j]]
                else:
                    return False

            return curr.terminating

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('abc')
obj.addWord('xyz')
asserter(lambda: obj.search('abc'), True)
asserter(lambda: obj.search('a.c'), True)
asserter(lambda: obj.search('ab'), False)
asserter(lambda: obj.search('.y.'), True)
