"""
    https://leetcode.com/discuss/interview-question/368482/Amazon-or-Phone-Screen-or-Count-Binary-Tree-Nodes-and-Find-Leaders

    Given an array [16, 18, 6, 7, 4, 1] return the "leaders". 
    An item is a leader if it is the larger than all numbers to its right. 
    In this example it would be [18, 7, 4, 1] for the leaders. 
    Discussed different approaches and runtimes, eventually doing it in O(n).
"""


def findTheLeader(nums):
    maxVal = max(nums)
    for i in range(len(nums)):
        if nums[i] == maxVal:
            return nums[i:]
    return nums


a = [16, 18, 6, 7, 4, 1]
print(findTheLeader(a))

a = [20, 18, 6, 7, 4, 1]
print(findTheLeader(a))

a = [20, 18, 6, 7, 4, 100]
print(findTheLeader(a))
