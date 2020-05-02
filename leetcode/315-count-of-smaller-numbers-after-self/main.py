"""
    1st: binary search
    - at each index, record a sort list with binary search
    - iterate the input again to find the count of smaller numbers with with binary search

    e.g. [5,2,6,1,2]
    0: [1, 2, 2, 5, 6], <- 3
    1: [1, 2, 2, 6],    <- 1
    2: [1, 2, 6],       <- 2
    3: [1, 2],          <- 0
    4: [2]              <- 0

    Time    O(N * (logN + K))
    Spac    O(N)
    124 ms, faster than 74.46% 
"""


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_arr = []
        result = []
        for num in nums[::-1]:
            idx = self.lowerBsearch(sorted_arr, num)
            result.append(idx)
            sorted_arr.insert(idx, num)

        return result[::-1]

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()

a = [5, 2, 6, 1, 2, 1]
print(s.countSmaller(a))


print("-----")

"""
    2nd: mergesort, learned from others
    
    ref:
    - https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution

    Time    O(NlogN)
    Space   O(N) we copy an extra list for mergesort
    152 ms, faster than 47.32%
"""


class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def divide(pairs):
            if len(pairs) == 1:
                return pairs
            mid = len(pairs) // 2
            left = divide(pairs[:mid])
            right = divide(pairs[mid:])
            return conquer(left, right)

        def conquer(left, right):
            sorted_arr = []
            i = j = 0
            # sort the numbers to a descending order
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    # crux: len(right) - j indicates the count of numbers in right subarray are less than left[i][0]
                    res[left[i][1]] += len(right) - j

                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1
            if i < len(left):
                sorted_arr += left[i:]
            if j < len(right):
                sorted_arr += right[j:]
            return sorted_arr

        if not nums:
            return []
        res = [0] * len(nums)
        # pairs of (num, idx)
        pairs = [(n, i) for i, n in enumerate(nums)]
        divide(pairs)
        return res


s = Solution()

a = [5, 2, 6, 1, 2, 1]
print(s.countSmaller(a))


print("-----")

"""
    3rd: Binary Indexed Tree + Prefix Sum
    - e.g. [5, 2, 6, 1, 2, 1]
            ^  ^  ^  ^  ^  ^
    rank = [3, 2, 4, 1, 2, 1] <- it means the rank of each of the number after input array is sorted

    num     rank    frequency(fenwick)  prefix sum/query(rank-1)
    1       1       [0<-,1,0,0,0]       0
    2       2       [0,1<-,1,0,0]       1
    1       1       [0<-,2,1,0,0]       0
    6       4       [0,2,1,0<-,1]       3
    2       2       [0,2<-,2,0,1]       2
    5       3       [0,2,2<-,1,1]       4

    - see idea.png for detail
    
    ref:
    - https://www.youtube.com/watch?v=2SVLYsq5W8M

    Time    O(NlogN)
    Space   O(N)
    100 ms, faster than 90.00%
"""


class BinaryIndexedTree(object):
    def __init__(self, n):
        self.fenwickTree = (n+1) * [0]

    def update(self, i, val):
        k = i + 1
        while k < len(self.fenwickTree):
            self.fenwickTree[k] += val
            k += k & -k

    def getSum(self, i):
        s = 0
        k = i + 1
        while k > 0:
            s += self.fenwickTree[k]
            k -= k & -k
        return s


class Solution(object):
    def countSmaller(self, nums):
        hashTable = {v: i+1 for i, v in enumerate(sorted(set(nums)))}

        tree = BinaryIndexedTree(len(hashTable))
        res = []
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            index = hashTable[num]
            res.append(tree.getSum(index-1))
            # update frequency
            tree.update(index, 1)
        return res[::-1]


s = Solution()

a = [5, 2, 6, 1, 2, 1]
print(s.countSmaller(a))
