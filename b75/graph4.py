# 207. Course Schedule
from collections import defaultdict
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

    def canFinishV2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        A simplification, using the blunt hammer known as Topological Sort DFS.
        Realized numCourses is not needed. Any courses not in the graph are trivially completable,
        so we can ignore them.
        """
        if not prerequisites:
            return True

        graph = defaultdict(set)
        for b, a in prerequisites:
            _ = graph[b]  # create key for b if DNE so we don't expand accidentally our graph later
            graph[a].add(b)

        visited = {}  # course -> bool. If false, still visiting, so is cycle

        def dfs(a):
            if a in visited:
                return visited[a]

            visited[a] = False
            finishable = all(dfs(b) for b in graph[a])
            visited[a] = True

            return finishable

        return all(dfs(course) for course in graph)


asserter(lambda: Solution().canFinishV2(2, [[1, 0], [0, 1]]), False)
asserter(lambda: Solution().canFinishV2(2, [[1, 0]]), True)
asserter(lambda: Solution().canFinishV2(5, [[1, 4], [2, 4], [3, 1], [3, 2]]), True)
