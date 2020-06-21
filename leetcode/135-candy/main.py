"""
    1st: brute force

    Time    O(N^2 + N)
    Space   O(N)

    LTE
    45 / 48 test cases passed.
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(ratings)):
            left = 0
            for j in range(i-1, -1, -1):
                if ratings[j] >= ratings[j+1]:
                    break
                left += 1
            right = 0
            for j in range(i+1, len(ratings)):
                if ratings[j] >= ratings[j-1]:
                    break
                right += 1
            res.append(max(left, right) + 1)
        return sum(res)


s = Solution()

a = [1, 0, 2]
print(s.candy(a))

a = [1, 2, 2]
print(s.candy(a))

a = [0]
print(s.candy(a))

a = [1, 0, 2, 3, 3, 1, 2]
print(s.candy(a))

a = [1, 2, 2, 2, 2, 2, 3]
print(s.candy(a))

print("-----")

"""
    2nd: min max 2 arrays
    - similar to lc915
    - from the front to the end, store the number of candies by comparing with the previous item
    - from the end to the front, store the number of candies by comparing with the previous item
    - the max of forwards[i] and backwards[i] is our result at each index

    e.g. 12, 4, 3, 11, 34, 34, 67
    ->    1, 1, 1,  2,  3,  1,  2
    <-    3, 2, 1,  1,  1,  1,  1
    -----------------------------
    max   3, 2, 1,  2,  3,  1,  2

    Time    O(3N)
    Space   O(2N)
    148 ms, faster than 51.87%
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        forwards = n * [1]
        backwards = n * [1]
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                forwards[i] = forwards[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                backwards[i] = backwards[i+1] + 1
        res = 0
        for i in range(n):
            res += max(forwards[i], backwards[i])
        return res
