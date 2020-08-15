"""
    1st: recursive dfs

    e.g. [1,2,3]
    1          2         3
    2,3 3,2   1,3  3,1    1,2 2,1

    select k from n number, it is a permutation problem
    therefore, the time complexity is nPk = n!/(n-k)!

    therefore, the crux is dfs(nums[:i]+arr[i+1:], prefix+[nums[i]])
    beats 32.64%
"""


class Solution(object):

    def __init__(self):
        self.result = []

    def permute(self, nums):
        self.dfs(nums, [])
        return self.result

    def dfs(self, cands, chosen):
        if len(cands) == 0:
            self.result.append(chosen)
        for i in range(len(cands)):
            self.dfs(cands[:i] + cands[i+1:], chosen + [cands[i]])


# s = Solution()
# print(s.permute([1, 2, 3]))

# iterative insertion
# e.g. [1,2,3]
#   1
#  ^ ^
#  2 2
#
#   2,1         1,2
#  ^ ^ ^       ^ ^ ^
#  3 3 3       3 3 3
# beats 32.64%


def permute1(nums):
    perms = [[]]
    for num in nums:  # for each number
        new_perms = []
        for perm in perms:  # for each temporary result
            for i in range(len(perm)+1):  # for each slot
                new_perms.append(perm[:i] + [num] + perm[i:])
        perms = new_perms
    return perms


print(permute1([1, 2, 3]))
