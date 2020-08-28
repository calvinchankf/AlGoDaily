"""
    1st approach: cache the result and put it back in the input

    Time    O(n)
    Space   O(n)
    44 ms, faster than 87.39%
"""


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        prev = chars[0]
        count = 1
        res = ""
        for i in range(1, len(chars)):
            c = chars[i]
            if c == prev:
                count += 1
            else:
                if count > 1:
                    res += prev + str(count)
                else:
                    res += prev
                prev = c
                count = 1
        if count > 1:
            res += prev + str(count)
        else:
            res += prev
        for i in range(len(res)):
            chars[i] = res[i]
        return res


s = Solution()

a = ["a", "a", "b", "b", "c", "c", "c"]
print(s.compress(a))

a = ["a"]
print(s.compress(a))

a = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(s.compress(a))

a = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c"]
print(s.compress(a))

a = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c"]
print(s.compress(a))

print("-----")

"""
    2nd: in-place with 2 pointers
"""


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0
        cur = chars[0]
        count = 1
        j = 0
        for i in range(1, len(chars)):
            c = chars[i]
            if c != cur:
                chars[j] = cur
                j += 1
                if count > 1:
                    countStr = str(count)
                    for x in countStr:
                        chars[j] = x
                        j += 1
                cur = c
                count = 1
            else:
                count += 1
        # print(cur, chars, j)
        if count > 0:
            chars[j] = cur
            j += 1
            if count > 1:
                countStr = str(count)
                for x in countStr:
                    chars[j] = x
                    j += 1
        return j
