"""
    1st: brute force
    - simulate the process

    Time    O(N^2)
    Space   O(N)
    64 ms, faster than 62.37%
"""


class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for _ in range(V):
            # left
            lowest = K
            for i in range(K-1, -1, -1):
                if heights[i] < heights[i+1]:
                    lowest = i
                elif heights[i] > heights[i+1]:
                    break
            if heights[lowest] < heights[K]:
                heights[lowest] += 1
                continue

            # right
            lowest = K
            for i in range(K+1, len(heights)):
                if heights[i] < heights[i-1]:
                    lowest = i
                elif heights[i] > heights[i-1]:
                    break
            if heights[lowest] < heights[K]:
                heights[lowest] += 1
                continue

            # K
            heights[K] += 1

        return heights
