from util import asserter


class Node:
    def __init__(self, key, nxt=None):
        self.key = key
        self.next = nxt

    def __eq__(self, other):
        if self and other:
            if self.key is not None and other.key is not None:
                return self.key == other.key and self.next == other.next
            return True
        return False


class LinkedList:
    def __init__(self, nodechain):
        self.head = nodechain

        while nodechain and nodechain.key is not None:
            nodechain = nodechain.next

        self.tail = nodechain  # should be Node(None)

    def search(self, k):
        curr = self.head
        while curr:
            if curr.key == k:
                return curr
            curr = curr.next
        return None

    def insert(self, k):
        self.tail.key = k
        newtail = self.tail
        self.tail.next = Node(None)
        self.tail = self.tail.next
        return newtail

    def delete(self, x):
        x.key = x.next.key
        x.next = x.next.next
        if x.key is None:
            self.tail = x

    def successor(self, x):
        curr = self.head
        smallest_successor = None
        while curr:
            if curr.key is not None and curr.key >= x.key and curr is not x:
                if smallest_successor is None or curr.key <= smallest_successor.key:
                    smallest_successor = curr
            curr = curr.next
        if smallest_successor is x:  # Nothing bigger than x found
            return None
        return smallest_successor

    def predecessor(self, x):
        pass

    def minimum(self):
        """
        Can't be O(1) if delete is O(1) because event if we maintain a stack of mins, when we delete a node that isn't
        min or max would require traversing the stack to find it, violating O(1) either in this method or the delete
        method.
        """
        curr = self.head
        smallest = None
        while curr:
            if curr.key is not None:
                if smallest is None or curr.key <= smallest.key:
                    smallest = curr
            curr = curr.next
        return smallest

    def maximum(self):
        pass


# 1-3-2-0-3
# Node(None) is sentinel/end node
rest2 = Node(0, Node(3, Node(None)))
second = Node(3, Node(2, rest2))
frst = Node(1, second)
ll = LinkedList(frst)
asserter(lambda: ll.search(0), Node(0, Node(3, Node(None))))
asserter(lambda: ll.search(4), None)
last = ll.insert(4)
# 1-3-2-0-3-4
asserter(lambda: ll.search(4), Node(4, Node(None)))
full_ll = ll
asserter(lambda: ll.successor(last), None)
asserter(lambda: ll.minimum(), rest2)
ll.delete(last)
# 1-3-2-0-3
asserter(lambda: ll.head, Node(1, Node(3, Node(2, Node(0, Node(3, Node(None)))))))
asserter(lambda: ll.tail, Node(None))
asserter(lambda: ll.successor(frst), Node(2, Node(0, Node(3, Node(None)))))
asserter(lambda: ll.minimum(), rest2)
ll.delete(frst)
# 3-2-0-3
asserter(lambda: ll.head, Node(3, Node(2, Node(0, Node(3, Node(None))))))
asserter(lambda: ll.tail, Node(None))
asserter(lambda: ll.successor(rest2), Node(2, Node(0, Node(3, Node(None)))))
asserter(lambda: ll.minimum(), rest2)
ll.delete(rest2)
# 3-2-3
asserter(lambda: ll.head, Node(3, Node(2, Node(3, Node(None)))))
asserter(lambda: ll.tail, Node(None))
asserter(lambda: ll.minimum(), Node(2, rest2))
