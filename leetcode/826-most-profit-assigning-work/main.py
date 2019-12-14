"""
    Here was my first approach, upper bound binary search

    1. group the difficulty and profit in an extra array A, sort them by difficulty
    2. need another extra array B to save the maxProfits up until each difficulty
    3. for each worker, upper bound binary search amongst A to get an index, add up the maxProfits[index] to the result
    
    Illustration on the steps with the below example:
    difficulty = [68, 35, 52, 47, 86]
    profit = [67, 17, 1, 81, 3]
    worker = [92, 10, 85, 84, 82]

    1. A = [(35, 17), (47, 81), (52, 1), (68, 67), (86, 3)]
    2. B = [17, 81, 81, 81, 81]
    3. idx from binary search = [4, -1, 3, 3, 3]
    so the result will be B[4] + B[-1] + B[3] + B[3] + B[3] = 81 + 0 + 81 + 81 + 81 = 324
    
    Time O(DlogD + WlogD)
    Space O(D+P)
    496 ms, faster than 9.80%
"""


class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        arr = []
        for i in range(len(difficulty)):
            arr.append((difficulty[i], profit[i]))
        arr = sorted(arr, key=lambda x: x[0])

        maxProfit, maxProfits = 0, []
        for _, gain in arr:
            maxProfit = max(maxProfit, gain)
            maxProfits.append(maxProfit)

        total = 0
        for person in worker:
            idx = self.uppperBsearch(arr, person) - 1
            if idx > -1:
                total += maxProfits[idx]

        return total

    def uppperBsearch(self, arr, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right)//2
            if target >= arr[mid][0]:
                left = mid + 1
            else:
                right = mid
        return right


s = Solution()

a = [2, 4, 6, 8, 10]
b = [10, 20, 30, 40, 50]
c = [4, 5, 6, 7]
print(s.maxProfitAssignment(a, b, c))

# diffculty not proportional to profit, 324
a = [68, 35, 52, 47, 86]
b = [67, 17, 1, 81, 3]
c = [92, 10, 85, 84, 82]
print(s.maxProfitAssignment(a, b, c))

# duplicate values, 553
a = [23, 30, 35, 35, 43, 46, 47, 81, 83, 98]
b = [8, 11, 11, 20, 33, 37, 60, 72, 87, 95]
c = [95, 46, 47, 97, 11, 35, 99, 56, 41, 92]
print(s.maxProfitAssignment(a, b, c))
