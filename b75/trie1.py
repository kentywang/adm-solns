from dataclasses import dataclass, field
from typing import ForwardRef, Optional

from util import asserter


@dataclass
class Node:
    terminating: bool = False
    children: dict[str, Optional[ForwardRef('Node')]] = field(default_factory=dict)


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Time: O(w)
        Space: O(w)
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
        Time: O(w)
        Space: O(1)
        """
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False

        return curr.terminating

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('abc')
asserter(lambda: obj.search('abc'), True)
asserter(lambda: obj.search('ab'), False)
asserter(lambda: obj.startsWith('abc'), True)
asserter(lambda: obj.startsWith('abc'), True)
