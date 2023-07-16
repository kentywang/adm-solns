"""
Hash table's worst case for search is O(n), not O(1).
So instead of hashing, we should take advantage of knowledge that the elements are all natural numbers up until some
fixed n. So it really could be a bit array where each index's value represents if the element is in the data structure.

Space: O(n)
Time (init): O(n) (reserving array size is probably O(1), but setting each element's value to False is O(n)
Time (insert): O(1)
Time (delete): O(1)
Time (search): O(1)
"""
from util import asserter


class DataStruct:
    def __init__(self, size):
        self.arr = [False] * size

    def insert(self, num: int):
        self.arr[num - 1] = True

    def delete(self, num: int):
        self.arr[num - 1] = False

    def search(self, num: int):
        return self.arr[num - 1]


ds = DataStruct(10)  # n = 10
ds.insert(2)
ds.insert(3)
ds.insert(5)
ds.insert(7)
asserter(lambda: ds.search(3), True)
asserter(lambda: ds.search(10), False)
ds.insert(10)
ds.delete(3)
asserter(lambda: ds.search(3), False)
asserter(lambda: ds.search(10), True)
