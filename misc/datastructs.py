from dataclasses import dataclass


class Heap:
    """
    Max heap
    """

    def __init__(self):
        self.q = []

    def push(self, x):
        newindex = len(self.q)
        self.q.append(x)
        self._siftup(newindex)

    def pop(self):
        if len(self.q) == 1:
            return self.q.pop()

        last = len(self.q) - 1

        self.q[0], self.q[last] = self.q[last], self.q[0]
        item = self.q.pop()
        self._siftdown(0)
        return item

    def _siftup(self, i):
        if i == 0:
            return

        parent = (i - 1) // 2
        if self.q[parent] < self.q[i]:
            self.q[i], self.q[parent] = self.q[parent], self.q[i]
            self._siftup(parent)

    def _siftdown(self, i):
        child1 = 2 * i + 1
        child2 = 2 * i + 2

        candidates = []

        if child1 >= len(self.q):  # no left child
            return
        if child2 >= len(self.q):  # no right child, but left child
            candidates.append(child1)
        else:
            # prioritize bigger child to compare with, as they should rise up
            candidates.extend([child1, child2] if self.q[child2] > self.q[child1] else [child2, child1])

        while candidates:
            c = candidates.pop()
            if self.q[c] > self.q[i]:
                self.q[i], self.q[c] = self.q[c], self.q[i]
                self._siftdown(c)  # continue sifting down the same element
                return


@dataclass
class DSUElement:
    root: str
    weight = 1


class DSU:
    def __init__(self):
        self.parent = {}

    def union_sets(self, x, y):
        a = self.find_root(x)
        b = self.find_root(y)

        if a != b:
            if self.parent[a].weight > self.parent[b].weight:
                self.parent[b].root = self.parent[a].root
                self.parent[a].weight += self.parent[b].weight
            else:
                self.parent[a].root = self.parent[b].root
                self.parent[b].weight += self.parent[a].weight

    def find_root(self, x):
        if x not in self.parent:
            self.parent[x] = DSUElement(x)

        if self.parent[x].root == x:
            return x

        self.parent[x].root = self.find_root(self.parent[x].root)
        return self.parent[x].root


dsu = DSU()
dsu.union_sets('a', 'b')
dsu.union_sets('c', 'b')
dsu.union_sets('d', 'c')
dsu.union_sets('b', 'k')
print(dsu.find_root('d'))
