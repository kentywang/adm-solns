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

        if child1 >= len(self.q):
            return
        if child2 >= len(self.q):
            candidates.append(child1)
        else:
            candidates.extend([child1, child2] if self.q[child2] > self.q[child1] else [child2, child1])

        while candidates:
            c = candidates.pop()
            if self.q[c] > self.q[i]:
                self.q[i], self.q[c] = self.q[c], self.q[i]
                self._siftdown(c)
                return
