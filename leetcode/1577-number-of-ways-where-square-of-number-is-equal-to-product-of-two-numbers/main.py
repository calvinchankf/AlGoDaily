from collections import Counter

"""
    1st: brute force + hashtable

    Time    O(MlogM + NlogN + M^2 + N^2)
    Space   O(M+N)
    936 ms, faster than 100.00%
"""


class Solution(object):
    def numTriplets(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        sq1 = [x**2 for x in nums1]
        sq2 = [x**2 for x in nums2]

        # print(sq1, sq2)

        R = len(sq1)
        C = len(sq2)

        prod1 = Counter()
        for i in range(R):
            for j in range(i+1, R):
                p = nums1[i] * nums1[j]
                prod1[p] += 1

        prod2 = Counter()
        for i in range(C):
            for j in range(i+1, C):
                p = nums2[i] * nums2[j]
                prod2[p] += 1

        # print(prod1, prod2)

        res = 0
        for i in range(R):
            x = sq1[i]
            if x in prod2:
                res += prod2[x]

        for i in range(C):
            x = sq2[i]
            if x in prod1:
                res += prod1[x]

        return res


s = Solution()


a = [7, 4]
b = [5, 2, 8, 9]
print(s.numTriplets(a, b))

a = [1, 1]
b = [1, 1, 1]
print(s.numTriplets(a, b))

a = [7, 7, 8, 3]
b = [1, 2, 9, 7]
print(s.numTriplets(a, b))

a = [4, 7, 9, 11, 23]
b = [3, 5, 1024, 12, 18]
print(s.numTriplets(a, b))

print("---")


a = [7, 4, 4]
b = [5, 2, 8, 9]
print(s.numTriplets(a, b))
