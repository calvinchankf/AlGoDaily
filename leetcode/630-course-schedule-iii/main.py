"""
    1st: recursion + hashtable
    TLE
"""


from heapq import *


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: (x[1], x[0]))
        return self.dfs(courses, 0, 0, {})

    def dfs(self, courses, i, cur, ht):
        if i == len(courses):
            return 0
        t, d = courses[i]
        key = (i, cur)
        if key in ht:
            return ht[key]
        take = 0
        if cur + t <= d:
            take = self.dfs(courses, i+1, cur + t, ht) + 1
        notTake = self.dfs(courses, i+1, cur, ht)
        ht[key] = max(take, notTake)
        return ht[key]


"""
    2nd: max heap
    - sort the courses by endTime
    - maintain an endTime when we iterate through the courses
    - push the duration into the heap
    - if the endTime > d unfortunity, we need remove the longest duration course from the maxheap
        - worst case: the current course has the longest duration, so we at most do heappop once
    - the remaining courses in the maxheap are result

    ref:
    - https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation

    Time    O(NlogN)
    Space   O(N)
    720 ms, faster than 39.94%
"""


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: (x[1], x[0]))
        maxheap = []
        endTime = 0
        for t, d in courses:
            endTime += t
            heappush(maxheap, -t)
            if endTime > d:
                negative_t = heappop(maxheap)
                endTime -= -negative_t
        return len(maxheap)
