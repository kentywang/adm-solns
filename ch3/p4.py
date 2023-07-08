from util import asserter


class Stack:
    def __init__(self):
        self.minimums = []
        self.stack: list = []

    def push(self, x):
        self.stack.append(x)

        if len(self.minimums) == 0:
            self.minimums.append(x)
        else:
            if x <= self.minimums[-1]:
                self.minimums.append(x)

    def pop(self):
        val = self.stack.pop()
        if self.minimums[-1] == val:
            self.minimums.pop()

        return val

    def findmin(self):
        return self.minimums[-1]


s = Stack()
s.push(1)
s.push(2)
s.push(0)
s.push(3)
s.push(0)
s.push(4)
asserter(lambda: s.findmin(), 0)
asserter(lambda: s.pop(), 4)
asserter(lambda: s.pop(), 0)
asserter(lambda: s.findmin(), 0)
asserter(lambda: s.pop(), 3)
asserter(lambda: s.pop(), 0)
asserter(lambda: s.findmin(), 1)
