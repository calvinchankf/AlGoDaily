"""
    1st approach: min and max 2 arrays
    - similar to lc135, lc1493
    - from the front to the end, store the max at each index
    - from the end to the front, store the min at each index
    - when max[i-1] <= max[i] <= min[i+1], it is the target index of the last item in the winter period

    Time    O(3n)
    Space   O(2n)
    200 ms, faster than 36.26%
"""


class Solution(object):
    def partitionDisjoint(self, T):
        """
        :type A: List[int]
        :rtype: int
        """
        greater = len(T) * [0]
        greater[0] = T[0]
        for i in range(1, len(T)):
            greater[i] = max(T[i], greater[i-1])
        # find the min from the end
        smaller = len(T) * [0]
        smaller[-1] = T[-1]
        for i in range(len(T)-2, -1, -1):
            smaller[i] = min(T[i], smaller[i+1])
        # when max[i-1] <= max[i] <= min[i+1], it is the target index of the last item in the winter period
        for i in range(len(T)-1):
            if i == 0:
                if greater[i] <= smaller[i+1]:
                    return i + 1
            else:
                now = greater[i]
                g = greater[i-1]
                s = smaller[i+1]
                if g <= now and now <= s:
                    return i+1
        # wont go here because the question mentions that there must be one result
        return -1


# 3
print(Solution().partitionDisjoint([5, -2, 3, 8, 6]))
# 4
print(Solution().partitionDisjoint([-5, -5, -5, -42, 6, 12]))
# 4
print(Solution().partitionDisjoint([5, -2, 3, -1, 6]))
# 4
print(Solution().partitionDisjoint([1, 2, 3, 4, 5, 6]))
# 1
print(Solution().partitionDisjoint([1, 1]))

print("-----")

"""
    2nd approach: min and max, concise logic
    - from the front to the end, store the max at each index
    - from the end to the front, store the min at each index
    - when max[i-1] <= min[i], it is the target index of the last item in the winter period

    e.g. 1
            5, 0, 3, 8, 6
    max ->  5, 5, 5, 8, 8
    min <-  3, 3, 3, 6, 6
                    ^
                    this is the partition point

    e.g. 2
            1, 1, 1, 0, 6, 12
    max ->  1, 1, 1, 1, 6, 12
    min <-  0, 0, 0, 0, 6, 12
                       ^
                       this is the partition point

    Time    O(3n)
    Space   O(2n)
    200 ms, faster than 36.26%
"""


class Solution(object):
    def partitionDisjoint(self, T):
        """
        :type A: List[int]
        :rtype: int
        """
        greater = len(T) * [0]
        greater[0] = T[0]
        for i in range(1, len(T)):
            greater[i] = max(T[i], greater[i-1])
        # find the min from the end
        smaller = len(T) * [0]
        smaller[-1] = T[-1]
        for i in range(len(T)-2, -1, -1):
            smaller[i] = min(T[i], smaller[i+1])
        # when max[i-1] <= max[i] <= min[i+1], it is the target index of the last item in the winter period
        for i in range(1, len(T)):
            if greater[i-1] <= smaller[i]:
                return i
        # wont go here because the question mentions that there must be one result
        return -1


# 3
print(Solution().partitionDisjoint([5, -2, 3, 8, 6]))
# 4
print(Solution().partitionDisjoint([-5, -5, -5, -42, 6, 12]))
# 4
print(Solution().partitionDisjoint([5, -2, 3, -1, 6]))
# 4
print(Solution().partitionDisjoint([1, 2, 3, 4, 5, 6]))
# 1
print(Solution().partitionDisjoint([1, 1]))
