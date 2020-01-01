"""
    similar to lc44, 712, 583

    questions to ask:
    - are the cost of add, delete, remove the same? yes
    - will there be empty strings? yes

    classic dynamic programming approach
    - https://www.youtube.com/watch?v=We3YDTzNXEk

    dp meaning:

    edit    |   insert
    -------------------
    delete  |   newstring

    insert means: insert one chracter to the horizontal string to form the vertical string
    delete means: delete one chracter from the horizontal string to form the vertical string
    edit means  : edit one chracter on the horizontal string to form the vertical string

    Time    O(word1 * word2)
    Space    O((word1+1) * (word2+1))
    196 ms, faster than 22.57%
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        construct a 2D array

        for empty word1[:0], empty string, we have to do len(word2) operations to form word2
        for empty word2[:0], empty string, we have to do len(word1) operations to form word1

        for other cells, put 0 for now
        """
        dp = []
        l1 = len(word1)
        l2 = len(word2)
        # since we from empty strings from word1 and word2
        # , we want to have a dp array of size l1+1 and l2+1
        for i in range(l1+1):
            temp = []
            for j in range(l2+1):
                if i == 0:
                    temp.append(j)
                elif j == 0:
                    temp.append(i)
                else:
                    temp.append(0)
            dp.append(temp)

        """
            for each cell,
            - if word1 == word2, use the upperleft value
            - if word1 != word2, get the min value from upperleft, left, above and +1
        """
        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    a = dp[i][j]
                    b = dp[i][j+1]
                    c = dp[i+1][j]
                    t = min(a, b, c)
                    dp[i+1][j+1] = t+1
        return dp[-1][-1]


print(Solution().minDistance("", ""))
print(Solution().minDistance("horse", "ros"))
print(Solution().minDistance("ros", "horse"))
print(Solution().minDistance("intention", "execution"))
print(Solution().minDistance("execution", "intention"))
