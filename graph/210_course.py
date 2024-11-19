from typing import List, Set


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def try_schedule(course: int, scheduled_coures: Set[int]) -> bool:
            if course in learnt:
                return True
            if course in scheduled_coures:
                return False
            scheduled_coures.add(course)
            success = True
            for pre in pdict[course]:
                success = success and try_schedule(pre, scheduled_coures)
                if not success:
                    return False
            schedule.append(course)
            learnt.add(course)
            scheduled_coures.remove(course)
            return True

        pdict: List[List[int]] = [[] for _ in range(numCourses)]
        schedule: List[int] = []
        learnt: Set[int] = set()
        being_scheduled = set()
        for course, pre in prerequisites:
            pdict[course].append(pre)
        for course in range(numCourses):
            if not try_schedule(course, being_scheduled):
                return []
            being_scheduled.clear()

        return schedule
