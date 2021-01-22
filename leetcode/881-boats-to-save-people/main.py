"""
    1st approach: sorting
    - keep in mind that each boat can carry 2 people at most only

    Time    O(nlogn)
    Space   O(1)
    452 ms, faster than 64.19%
"""


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i = 0
        j = len(people) - 1
        res = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                res += 1
                i += 1
                j -= 1
            elif people[j] <= limit:
                res += 1
                j -= 1
            elif people[i] <= limit:
                res += 1
                i += 1
            else:
                break
        return res


s = Solution()

# 1
a = [5]
b = 5
print(s.numRescueBoats(a, b))

# 1
a = [2, 1]
b = 3
print(s.numRescueBoats(a, b))

# 3
a = [3, 2, 2, 1]
b = 3
print(s.numRescueBoats(a, b))

# 4
a = [3, 5, 3, 4]
b = 5
print(s.numRescueBoats(a, b))

# 4
a = [4, 4, 10, 1, 2, 2, 2]
b = 10
print(s.numRescueBoats(a, b))

# 11
a = [2, 49, 10, 7, 11, 41, 47, 2, 22, 6, 13, 12, 33, 18, 10, 26, 2, 6, 50, 10]
b = 50
print(s.numRescueBoats(a, b))

"""
    followup: what if a boat can carry more than 2 people?
"""
