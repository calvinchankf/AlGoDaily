from collections import Counter
import heapq

"""
    1st approach: min heap
    - exactly the same as lc1286
    - put the numbers into a min heap
    - pop the heap and put the item into a "straight" array if the pop == straight[-1] + 1, else put the poped item into a dump array
    - if the straight array is of size W, put the dumps back to the heap

    Time    O(NlogN + NlogK)
    Space   O(N)
    488 ms, faster than 23.83% 
"""


class Solution(object):
    def isNStraightHand(self, nums, k):
        nums.sort()
        minheap = []
        res = []
        for x in nums:
            if len(minheap) > 0 and minheap[0][0] + 1 == x and len(minheap[0][1]) < k:
                head, arr = heappop(minheap)
                arr.append(x)
                if len(arr) == k:
                    res.append(arr)
                else:
                    heappush(minheap, (x, arr))
            else:
                if k == 1:
                    res.append([x])
                else:
                    heappush(minheap, (x, [x]))
        return len(minheap) == 0


a = [1, 2, 3, 6, 2, 3, 4, 7, 8]
b = 3
print(Solution().isNStraightHand(a, b))

a = [1, 2, 3, 6, 2, 3, 4, 7, 8, 9, 10, 11]
b = 3
print(Solution().isNStraightHand(a, b))

a = [1, 2, 3, 6, 2, 3, 4, 7, 8, 9, 10, 12]
b = 3
print(Solution().isNStraightHand(a, b))

a = [1, 2, 3, 4, 5]
b = 4
print(Solution().isNStraightHand(a, b))

a = [5, 1]
b = 2
print(Solution().isNStraightHand(a, b))

print("-----")


"""
    1st: sort + hashtable
    - put every number counter
    - sort the array
    - for each unused number, try to see if we can form a sequence(in length of K)

    Time    O(NlogN + NK)
    Space   O(N)
    212 ms, faster than 61.09%
"""


class Solution(object):
    def isNStraightHand(self, nums, k):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        nums.sort()
        counter = Counter(nums)
        for i in range(len(nums)):
            x = nums[i]
            if x not in counter:
                continue
            seq = [x]
            cur = x
            counter[cur] -= 1
            if counter[cur] == 0:
                del counter[cur]
            while cur+1 in counter and len(seq) < k:
                cur += 1
                seq.append(cur)
                counter[cur] -= 1
                if counter[cur] == 0:
                    del counter[cur]
            if len(seq) != k:
                return False
        return True
