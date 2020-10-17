"""
    1st approach: stack + hashtable
    - similar to leetcode316, 331, 735, 901, 1081
    - first count the number of occurence for each character
    - then we use a stack to store the temp result as we move forward
        - when the current character is lexicographicallly less than stack[-1] and stack[-] still has occurence larger than 0, we pop the stack
    - we push the current character onto the stack
    - we can use a hashtable to indicate which characters are currently in the stack

    Time    O(n)
    Space   O(n)
"""
class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type text: str
        :rtype: str
        """
        count = 26 * [0]
        for c in s:
            idx = ord(c) - ord('a')
            count[idx] += 1
        stack = []
        used = 26 * [False]
        for c in s:
            idx = ord(c) - ord('a')
            count[idx] -= 1
            if used[idx] == True:
                continue
            while len(stack) > 0 and stack[-1] > c and count[ord(stack[-1]) - ord('a')] > 0:
                pop = stack.pop()
                used[ord(pop) - ord('a')] = False
            stack.append(c)
            used[idx] = True
        return ''.join(stack)
