"""
    1st approach: hashset
    
    Time    O(n)
    Space   O(n)
    56 ms, faster than 39.07%
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hs = set()
        for num in nums:
            if num not in hs:
                hs.add(num)
            else:
                return num
        return -1


print(Solution().findDuplicate([1, 3, 4, 2, 2]))
print(Solution().findDuplicate([3, 1, 3, 4, 2]))
print(Solution().findDuplicate([2, 2, 1]))
print(Solution().findDuplicate([1, 3, 4, 2, 5, 6, 7, 2, 9, 8]))

print("-------------------------")


"""
    classic approach: 2 pointers like linked list cycle ii

    slow pointer: runs 1 steps at a time
    fast pointer: runs 2 steps at a time
    
    index:0  1  2  3  4  5  6  7  8  9
    e.g. [1, 3, 4, 2, 5, 6, 7, 2, 9, 8]

    slow pointer path:
    1 -> 3 -> 2 -> 4 -> 5 -> 6

    fast pointer path:
    1 -> (3) -> 2 -> (4) -> 5 -> (6) -> 7 -> (2) -> 4 -> (5) -> 6

    there must be a duplicate point such that they reach to the same number

    to find out that point, see ../142-linked-list-cycle-ii

    since 2 * slow pointer steps = fast pointer steps
    if we run
    - 1 pointer again from the start point
    - 1 pointer again from the meet point
    they will meet at the duplicate number

    P.S. This work only because it is from 1 to N inclusive, such that any number would never point to an go-out-of-boundary index
          0  1  2  3  4
    e.g. [1, 3, 4, 2, 2]

    Time    O(2n)
    Space   O(1)
    68 ms, faster than 31.83%
"""


class Solution(object):
    def findDuplicate(self, nums):
        # find the end of the cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # 2 (a + b) = a + b + c + b => a = c
        p1 = nums[0]
        p2 = slow  # or fast
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1  # or p2


print(Solution().findDuplicate([1, 3, 4, 2, 2]))
print(Solution().findDuplicate([3, 1, 3, 4, 2]))
print(Solution().findDuplicate([2, 2, 1]))
print(Solution().findDuplicate([1, 3, 4, 2, 5, 6, 7, 2, 9, 8]))
