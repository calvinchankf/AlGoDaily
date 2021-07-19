"""
    1st: backtracking
    - this is a textbook problem: Hungarian Matching Algorithm

    Time    
"""


class Solution(object):
    def maximumInvitations(self, grid):
        M, N = len(grid), len(grid[0])
        matches = N * [-1]  # girls' mate

        def dfs(boy, asked):

            # ask every girl
            for girl in range(N):

                # guard: the girl is available to this boy AND has not been asked before
                if grid[boy][girl] == 0 or asked[girl] == True:
                    continue
                asked[girl] = True  # mark her as asked

                # if the girl does not have a mate or her mate has been matched to someone else
                if matches[girl] == -1 or dfs(matches[girl], asked):
                    # we match her to this boy
                    matches[girl] = boy
                    return True
            return False

        res = 0
        # For every boy
        for i in range(M):
            asked = N * [False]
            if dfs(i, asked):
                res += 1

        return res
