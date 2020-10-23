"""
    approach during contest binary search

    e.g. [1,2,3,10,4,2,3,5]
    forward = [1, 2, 3, 10]
    backward = [2, 3, 5]

    then we do binary search to find the longest combined array
    0 -> [1] + [2,3,5]
    1 -> [1,2] + [2,3,5] <- length = 5, which is longest
    2 -> [1,2,3] + [3,5] <- length = 5, which is longest too
    3 -> [1,2,3,10] + []

    Time    O(2N + NlogN)
    Space   O(2N)
    2732 ms, faster than 5.07%
"""


class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        forward = [arr[0]]
        for i in range(1, n):
            if arr[i-1] <= arr[i]:
                forward.append(arr[i])
            else:
                break

        backward = [arr[-1]]
        for i in range(n-2, -1, -1):
            if arr[i] <= arr[i+1]:
                backward.insert(0, arr[i])
            else:
                break

        k = max(len(forward), len(backward))
        for i in range(len(forward)):
            j = self.lowerBsearch(backward, forward[i])
            # print(i, j)
            if 0 <= j < len(backward):
                temp = i + 1 + len(backward) - j
                k = max(k, temp)
        return max(n - k, 0)

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

a = [1,2,3,10,4,2,3,5]
print(s.findLengthOfShortestSubarray(a))

a = [5,4,3,2,1]
print(s.findLengthOfShortestSubarray(a))

a = [1,2,3]
print(s.findLengthOfShortestSubarray(a))

a = [1]
print(s.findLengthOfShortestSubarray(a))

a = [1,2,2,2,2,2,3,1,7,5,1,2,2,2,2,2,2,5,6]
print(s.findLengthOfShortestSubarray(a))

a = [0,16,3,13,14,11,1,24,20,20,18,15,20]
print(s.findLengthOfShortestSubarray(a))

print("-----")


"""
    2nd: 2 pointers
    - same logic to come up with forward and backward arrays
    - but use 2 pointers to find out the max length of combined array from 2 ends

    e.g. [1,2,3,10,4,2,3,5]
    forward = [1, 2, 3, 10]
    backward = [2, 3, 5]

    then we use 2 pointers to find the longest combined array
    [1, 2, 3, 10], [2,3,5]
     ^              ^       = the longest length k of combined array = 4
    [1, 2, 3, 10], [2,3,5]
        ^           ^       = the longest length k of combined array = 5
    [1, 2, 3, 10], [2,3,5]
           ^          ^     = the longest length k of combined array = 5
    [1, 2, 3, 10], [2,3,5]
               ^          ^ = the longest length k of combined array = 4
    
    So the result is len(arr)-k = 8 - 5 = 3

    Time    O(3N)
    Space   O(2N)
    608 ms, faster than 73.26%
"""
class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        forward = [arr[0]]
        for i in range(1, n):
            if arr[i-1] <= arr[i]:
                forward.append(arr[i])
            else:
                break

        backward = [arr[-1]]
        for i in range(n-2, -1, -1):
            if arr[i] <= arr[i+1]:
                backward.insert(0, arr[i])
            else:
                break

        k = max(len(forward), len(backward))
        i, j = 0, 0
        while i < len(forward) and j < len(backward):
            if forward[i] <= backward[j]:
                temp = i + 1 + len(backward) - j
                k = max(k, temp)
                i += 1
            else:
                j += 1
        return max(n - k, 0)

s = Solution()

a = [1,2,3,10,4,2,3,5]
print(s.findLengthOfShortestSubarray(a))

a = [5,4,3,2,1]
print(s.findLengthOfShortestSubarray(a))

a = [1,2,3]
print(s.findLengthOfShortestSubarray(a))

a = [1]
print(s.findLengthOfShortestSubarray(a))

a = [1,2,2,2,2,2,3,1,7,5,1,2,2,2,2,2,2,5,6]
print(s.findLengthOfShortestSubarray(a))

a = [0,16,3,13,14,11,1,24,20,20,18,15,20]
print(s.findLengthOfShortestSubarray(a))