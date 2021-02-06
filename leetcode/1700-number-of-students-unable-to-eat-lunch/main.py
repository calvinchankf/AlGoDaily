from collections import Counter

"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    32 ms, faster than 100.00%
"""


class Solution(object):
    def countStudents(self, students, sandwiches):
        n = len(students)
        counter = Counter(students)
        for i in range(n):
            s = sandwiches[i]
            if s in counter and counter[s] > 0:
                counter[s] -= 1
            else:
                return n - i
        return 0
