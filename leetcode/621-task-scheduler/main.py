import heapq
from collections import *

"""
    1st approach: maxheap
    - similar to lc358
    1. count occurence for each task
    2. in each iteration
        - pop the tasks from maxheap n+1 times
        - put the tasks back to the queue with decremented count
    3. remove trailing '-'(idle)

    Time    O(Nlog26) -> O(N)
    Space   O(N)
    744 ms, faster than 26.51%
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # count occurence for each task
        counter = Counter(tasks)
        pq = []
        for task in counter:
            heapq.heappush(pq, (-counter[task], task))
        res = []
        while len(pq) > 0:
            arr = []
            # pop the tasks from maxheap
            for _ in range(n+1):
                if len(pq) > 0:
                    count, task = heapq.heappop(pq)
                    res.append(task)
                    arr.append((count, task))
                else:
                    res.append("-")
            # put the tasks back to the queue with decremented count
            for count, task in arr:
                if abs(count) > 1:
                    heapq.heappush(pq, (count+1, task))
        # remove trailing '-'(idle)
        while len(res) > 0:
            if res[-1] == '-':
                res.pop()
            else:
                break
        # res is the list of tasks
        return len(res)


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B", "C", "C"], 2))
print(Solution().leastInterval(
    ["A", "A", "A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D"], 2))

print('-----')

"""
    2nd: greedy?
    - sort the tasks by frequency
    - the total time is the most frequent task with the idle time in between
    - calculate the number of vacancies we can use to insert the less frequent tasks
    - the result = number of tasks + idle time

    e.g.
    A:5
    B:3
    C:2
    D:1

    => A x x A x x A x x A x x A
    => A B x A B x A B x A x x A
    => A B C A B C A B x A x x A
    => A B C A B C A B D A x x A

    Time    O(N)
    Space   O(N)
    436 ms, faster than 79.75%
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n

        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B", "C", "C"], 2))
print(Solution().leastInterval(
    ["A", "A", "A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D"], 2))
