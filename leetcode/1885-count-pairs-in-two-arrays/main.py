"""
    1st: binary srach
    
    since   a + b > c + d
    is      a - c > d - b

    therefore   nums1[i] + nums1[j] > nums2[i] + nums2[j]
    is          -(nums2[i] - nums1[i]) > nums2[j] - nums1[j]

    Time    O(NlogN -> NlogN)   binary search takes O(logN) but python arr.insert() takes O(N)
    Space   O(N)
    7872 ms, faster than 100.00%
"""


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        arr = []
        res = 0
        for i in range(n-1, -1, -1):
            d = nums2[i] - nums1[i]
            smallerCount = self.lowerBsearch(arr, -d)
            j = self.lowerBsearch(arr, d)
            res += smallerCount
            arr.insert(j, d)
        return res

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


"""
    2nd: Binary Index Tree (BIT)
    - similar to lc307, 315
    - it is an optimized approach to 1st approach
    - we create a BIT to store the count at every diff

    Below is the illustration of using a BIT
    e.g. Let's say we have a list of diffs:
    diffs = [7, 1, 3, 2, 9, 2, 1]
    
    We dedup it and sort it:
    diffs = [1, 2, 3, 7, 9]

    Then we create a BIT, it is used to count the ocurrence for every number
    when we iterate the input from the back
    
    diffs       1, 2, 3, 7, 9
    BIT     [0, 0, 0, 0, 0, 0]

    How BIT works?
    e.g. when we search 3, binary search return 2, so we increment BIT[2] (BIT will +1 on your idx)
    BIT     [0, 0, 0, 1, 0, 0] <= it means now, we have 1 number <= 3 

    search 3 again,
    BIT     [0, 0, 0, 2, 0, 0] <= it means now, we have 2 numbers <= 3

    search 9,
    BIT     [0, 0, 0, 2, 0, 1] <= it means now, we have 2 numbers <= 3, and 3 numbers <= 9

    search 2,
    BIT     [0, 0, 1, 2, 0, 1] <= it means now, we have 1 number <=2, 2 numbers <= 3, and 3 numbers <= 9

    and so on....

    Time    O(NlogN)    BIT takes O(logN)
    Space   O(N)
    4796 ms, faster than 100.00%
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

    def getRangeSum(self, i, j):  # no-use here
        return self.getSum(j) - self.getSum(i-1)


class Solution(object):
    def countPairs(self, nums1, nums2):
        n = len(nums1)

        diffSet = set()
        for i in range(n):
            diffSet.add(nums2[i] - nums1[i])
        diffs = list(diffSet)
        diffs.sort()
        tree = BinaryIndexedTree(len(diffs))

        res = 0
        for i in range(n-1, -1, -1):
            d = nums2[i] - nums1[i]
            # search from the sort diffs
            smallerCount = self.lowerBsearch(diffs, -d) - 1
            res += tree.getSum(smallerCount)
            # search for the index j to increment the count
            j = self.lowerBsearch(diffs, d)
            tree.update(j, 1)  # we increment at index j
        return res

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
