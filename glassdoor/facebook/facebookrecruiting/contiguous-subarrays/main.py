"""
    https://leetcode.com/discuss/interview-question/742523/Facebook-or-Prep-question-or-Contiguous-Subarrays-O(n)-solution

    Contiguous Subarrays
    You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfills the following conditions:
    The value at index i must be the maximum element in the contiguous subarrays, and
    These contiguous subarrays must either start from or end on index i.
    
    Signature
    int[] countSubarrays(int[] arr)
    
    Input
    Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
    Size N is between 1 and 1,000,000
    
    Output
    An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
    
    Example:
    arr = [3, 4, 1, 6, 2]
    output = [1, 3, 1, 5, 1]
    
    Explanation:
    For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
    For index 1 - [4], [3, 4], [4, 1]
    For index 2 - [1]
    For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
    For index 4 - [2]
    So, the answer for the above input is [1, 3, 1, 5, 1]
"""


"""
    similar to lc739
"""
def countSubarrays(nums):
    n = len(nums)
    
    forward = n * [1]
    stack = []
    for i in range(n):
        while len(stack) > 0 and stack[-1][0] < nums[i]:
            _, j = stack.pop()
            forward[j] = i - j
        stack.append((nums[i], i))
    while len(stack) > 0:
        _, j = stack.pop()
        forward[j] = n - j
    
    backward = n * [1]
    stack = []
    for i in range(n-1,-1,-1):
        while len(stack) > 0 and stack[-1][0] < nums[i]:
            _, j = stack.pop()
            backward[j] = j - i
        stack.append((nums[i], i))
    while len(stack) > 0:
        _, j = stack.pop()
        backward[j] = j + 1

    res = []
    for i in range(n):
        res.append(forward[i] + backward[i] - 1)

    return res

a = [3, 4, 1, 6, 2]
print(countSubarrays(a))