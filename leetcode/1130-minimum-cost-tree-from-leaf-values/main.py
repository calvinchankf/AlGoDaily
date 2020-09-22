"""
    1st: greedy
    - similar to lc1046
    1. find the minimum number
    2. compare its left and right and the cost = min(left, right) * dip
    3. remove itself from the list
    4. repeat 1-3 until there is only one item left

    e.g. [6,2,4,7,2,3]

    [6, 2, 4, 7, 2, 3]
    [6, 4, 7, 2, 3],    2 is the smallest, pop 2, cost = min(6, 4) * 2 = 8
    [6, 4, 7, 3],       2 is the smallest, pop 2, cost = min(7, 3) * 2 = 6
    [6, 4, 7],          3 is the smallest, pop 3, cost = 7 * 3 = 21
    [6, 7]              4 is the smallest, pop 4, cost = min(6, 7) * 4 = 24
    [7]                 6 is the smallest, pop 6, cost = 6 * 7 = 42
    resutl = 8 + 6 + 21 + 24 + 42 = 101

    ref:
    - https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space

    Time    O(N^2)
    Space   O(1)
    60 ms, faster than 47.03%
"""


class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        res = 0
        while len(A) > 1:
            i = A.index(min(A))
            neighbors = []
            if i-1 >= 0:
                neighbors.append(A[i-1])
            if i+1 < len(A):
                neighbors.append(A[i+1])
            pop = A.pop(i)
            cost = min(neighbors) * pop
            print(cost)
            res += cost
        return res


"""
    2nd: stack
    - when the current number is larger then the stack[-1], it means stack[-1] is the local minimum amongst nums[i-1], nums[i], nums[i-1]
    - so we should pop the stack, and add the cost = min(left, right) to our result
    - we repeat this until the stack has only one legit item left

    e.g. [6,2,4,7,2,3]
    idx 0: stack = [inf, 6]
    idx 1: stack = [inf, 6, 2]
    idx 2: since 4 > stack[-1] = 2, stack-pop the 2, cost = min(6, 4) * 2 = 8
    idx 2: stack = [inf, 6, 4]
    idx 3: since 7 > stack[-1] = 4, stack-pop the 4, cost = min(6, 7) * 4 = 24
    idx 3: since 7 > stack[-1] = 6, stack-pop the 6, cost = 6 * 7 = 42
    idx 3: finally, nothing we can pop,  stack = [inf, 7]
    idx 4: stack = [inf, 7, 2]
    idx 5: since 3 > stack[-1] = 2, stack-pop the 2, cost = min(2, 3) * 3 = 6
    idx 5: stack = [inf, 7, 3]
    finally, 2 items remain, we should add the cost 7*3 = 21 to the result

    result = 8 + 24 + 42 + 6 + 21 = 101

    ref:
    - https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space

    Time    O(N)
    Space   O(N)
    28 ms, faster than 94.05%
"""


class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        res = 0
        stack = [sys.maxsize]
        for num in A:
            while stack[-1] <= num:
                dip = stack.pop()
                # cost = min(left, right) * dip
                cost = dip * min(stack[-1], num)
                res += cost
            stack.append(num)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
