# 207. Course Schedule
from typing import List

from util import asserter

"""
- We can tolerate cycles existing, as long as they aren't at the beginning
- Try doing courses with no prereqs. Once we do a course, remove them from each of the other lists
- When courses without prereqs are exhausted, we can't do more 

Time: O(n^2) 
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: set() for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].add(b)

        finished = set()
        while True:
            reqs_met = {course: reqs for course, reqs in graph.items() if len(reqs - finished) == 0}
            if len(reqs_met):
                for course in reqs_met:
                    graph.pop(course)
                    finished.add(course)

                    if len(finished) == numCourses:
                        return True

            else:
                return False


asserter(lambda: Solution().canFinish(2, [[1, 0], [0, 1]]), False)
asserter(lambda: Solution().canFinish(2, [[1, 0]]), True)
