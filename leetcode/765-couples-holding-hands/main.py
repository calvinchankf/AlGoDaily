from typing import List

"""
    1st: optimized BFS
    - similar to lc854
    - in BFS, we dont need to generate all permuation of swap(i,j) in every step
    - we can instead target the leftmost number at i+1 one by one to makes S more simliar to our target
        so that we can reduce the time complexity
    
    e.g. [2, 5, 4, 7, 1, 6, 3, 0]
             ^              ^
         [2, 3| 4, 7, 1, 6, 5, 0] <- the pair before | is fullfiled
                   ^        ^
         [2, 3, 4, 5| 1, 6, 7, 0] <- the pair before | is fullfiled
                         ^     ^
         [2, 3, 4, 5, 1, 0, 7, 6] <- the whole array is fullfiled

    
    Time    O(N^2)
    Space   O(N)
    44 ms, faster than 25.91%
"""


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        ht = {}
        ht[tuple(row)] = True
        q = [(row, 0)]
        while len(q) > 0:
            temp, steps = q.pop(0)
            if self.isPairedUp(temp):
                return steps
            for i, j in self.getCandidates(temp):
                clone = temp[:]
                clone[i], clone[j] = clone[j], clone[i]
                key = tuple(clone)
                if key in ht:
                    continue
                ht[key] = True
                q.append((clone, steps+1))
        return -1

    def isPairedUp(self, arr):
        i = 0
        while i < len(arr):
            if arr[i] % 2 == 0:
                if arr[i+1] != arr[i] + 1:
                    return False
            else:
                if arr[i+1] != arr[i] - 1:
                    return False
            i += 2
        return True

    def getCandidates(self, arr):
        i = 0
        while i < len(arr):
            if arr[i] % 2 == 0:
                if arr[i+1] != arr[i] + 1:
                    break
            else:
                if arr[i+1] != arr[i] - 1:
                    break
            i += 2
        # we only look for the candidate to swap
        # e.g [2, 5, 4, 7, 1, 6, 3, 0]
        #         ^              ^
        # so the next stage becomes [2, 3| 4, 7, 1, 6, 5, 0] such that the leftmost pair is sorted
        partner = None
        if arr[i] % 2 == 0:
            partner = arr[i] + 1
        else:
            partner = arr[i] - 1
        # print(i, partner)
        candidates = []
        for j in range(i+1, len(arr)):
            if arr[j] == partner:
                candidates.append((i+1, j))
        # print(candidates)
        return candidates


s = Solution()

a = [0, 2, 1, 3]
print(s.minSwapsCouples(a))

a = [3, 2, 0, 1]
print(s.minSwapsCouples(a))

a = [2, 5, 4, 1, 0, 3]
print(s.minSwapsCouples(a))

a = [0, 9, 8, 5, 7, 2, 1, 3, 4, 6]
print(s.minSwapsCouples(a))

a = [5, 4, 2, 6, 3, 1, 0, 7]
print(s.minSwapsCouples(a))

print("-----")


"""
    2nd: array
    - optimze the 1st approach
    - in the 1st approach, we observe that we always get only one pair of indices from getCandidates()
    - so means that BFS is not necessary

    Time    O(N^2)
    Space   O(N)
    40 ms, faster than 33.41%
"""


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        arr = row[:]
        i = 0
        res = 0
        while i < len(arr):
            if self.isPairedUp(arr):
                return res
            # move forward to find the next unpair numbers at indices (i, i+1)
            while i < len(arr):
                if arr[i] % 2 == 0:
                    if arr[i+1] != arr[i] + 1:
                        break
                else:
                    if arr[i+1] != arr[i] - 1:
                        break
                i += 2
            # calculate the target for number at index i
            partner = None
            if arr[i] % 2 == 0:
                partner = arr[i] + 1
            else:
                partner = arr[i] - 1
            # look for the target in the rest of the array, and swap(i+1, j) so to fullfil numbers at (i, i+1)
            for j in range(i+1, len(arr)):
                if arr[j] == partner:
                    arr[i+1], arr[j] = arr[j], arr[i+1]
                    break
            # record & iterate
            res += 1
            i += 2

    def isPairedUp(self, arr):
        i = 0
        while i < len(arr):
            if arr[i] % 2 == 0:
                if arr[i+1] != arr[i] + 1:
                    return False
            else:
                if arr[i+1] != arr[i] - 1:
                    return False
            i += 2
        return True


s = Solution()

a = [0, 2, 1, 3]
print(s.minSwapsCouples(a))

a = [3, 2, 0, 1]
print(s.minSwapsCouples(a))

a = [2, 5, 4, 1, 0, 3]
print(s.minSwapsCouples(a))

a = [0, 9, 8, 5, 7, 2, 1, 3, 4, 6]
print(s.minSwapsCouples(a))

a = [5, 4, 2, 6, 3, 1, 0, 7]
print(s.minSwapsCouples(a))
