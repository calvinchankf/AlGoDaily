"""
    dynamic programming, learned from the others

    the idea is
    1. every glass would fill up 2 glasses below it with excess amount of champagne
    2. so we can build a 2d array, and calculate the amount of champagne for every glass in a bottom-up fashion

    ref:
    - https://www.youtube.com/watch?v=NfPWhbKbuJg

    Time    O(N^2) n(n+1)/2
    Space   O(N^2)
    68ms beats 91.84%
"""
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = []
        for x in range(1, query_row + 2):
            dp.append(x * [0])
        
        dp[0][0] = poured
        
        for i in range(query_row):
            for j in range(len(dp[i])):
                leftover = (dp[i][j] - 1) / 2.0 # excess amount of champagne
                if leftover > 0:
                    dp[i+1][j] += leftover
                    dp[i+1][j+1] += leftover
        
        if dp[query_row][query_glass] <= 1:
            return dp[query_row][query_glass]
        return 1