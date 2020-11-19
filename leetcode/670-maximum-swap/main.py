"""
    1st approach: brute-force
    - try all the pairs to swap
    - find the max number
    - since the input is at most 1x10^8, there are at most 8*7 trials

    Time    O(logN x logN x logN)
    Space   O(logN) save the digit
    28 ms, faster than 77.81% 
"""


class Solution(object):
    def maximumSwap(self, num):
        digits = [int(c) for c in str(num)]
        n = len(digits)
        res = num
        for i in range(n):
            for j in range(i+1, n):
                digits[i], digits[j] = digits[j], digits[i]
                res = max(res, self.getNum(digits))
                digits[i], digits[j] = digits[j], digits[i]
        return res

    def getNum(self, digits):
        total = 0
        for d in digits:
            total = total*10 + d
        return total


"""
    2nd: greedy, learned from others
    - if there is a larger digit that occurs later, we know that the best swap must occur with the digit we are currently considering

    e.g. 98368
         01234 <- indices
    ht = {
        9: 0,
        8: 4,
        3: 2,
        6: 3
    }

    98368
    ^       no number is larger than 9
     ^      only 9 is larger than 8, but the index of 9 is smaller than the current index
      ^     8 is larger than 3, and the index of 8 = 4 which is larger than the current index. So this is the answer

    Time    O(N)
    Space   O(N)
    84 ms, faster than 20.53%
"""


class Solution(object):
    def maximumSwap(self, num):
        nums = [int(c) for c in str(num)]
        n = len(nums)
        ht = {}
        for i in range(n):
            x = nums[i]
            ht[x] = i
        for i in range(n):
            x = nums[i]
            for d in range(9, x, -1):
                if d in ht and ht[d] > i:
                    j = ht[d]
                    nums[i], nums[j] = nums[j], nums[i]
                    return self.getNum(nums)
        return num

    def getNum(self, digits):
        total = 0
        for d in digits:
            total = total*10 + d
        return total


s = Solution()
print(s.maximumSwap(98368))
