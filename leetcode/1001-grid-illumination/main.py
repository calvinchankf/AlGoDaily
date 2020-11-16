from collections import Counter

"""
    1st: hashtablesssss

"""
class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        lampSet = set()
        row_ht = Counter()
        col_ht = Counter()
        diag_ht = Counter() # topleft -> bottomright
        antiDiag_ht = Counter() #topright -> bottomleft
        for i, j in lamps:
            lampSet.add((i, j))
            row_ht[i] += 1
            col_ht[j] += 1
            diag_ht[i-j] += 1
            antiDiag_ht[i+j] += 1
        
        
        res = []
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1),(1, 0), (1, -1), (0, -1), (-1, -1)]
        for i, j in queries:
            
            # see if the cell is illuminated
            if i in row_ht or j in col_ht or i-j in diag_ht or i+j in antiDiag_ht:
                res.append(1)
            else:
                res.append(0)
            
            # gather itself and 8 adjacent lamps <- neighbours
            neighbours = [(i, j)]
            for di, dj in dirs:
                if 0 <= i+di < N and 0 <= j+dj < N:
                    neighbours.append((i+di, j+dj))
            
            # find the lamps from the neighbours
            # remember to remove the found lamps
            lampsToRemove = []
            for nb in neighbours:
                if nb in lampSet:
                    lampsToRemove.append(nb)
                    lampSet.remove(nb)
            
            # decrement the counts
            for _i, _j in lampsToRemove:
                if _i in row_ht:
                    row_ht[_i] -= 1
                    if row_ht[_i] == 0: del row_ht[_i]
                if _j in col_ht:
                    col_ht[_j] -= 1
                    if col_ht[_j] == 0: del col_ht[_j]
                if _i-_j in diag_ht:
                    diag_ht[_i-_j] -= 1
                    if diag_ht[_i-_j] == 0: del diag_ht[_i-_j]
                if _i+_j in antiDiag_ht:
                    antiDiag_ht[_i+_j] -= 1
                    if antiDiag_ht[_i+_j] == 0: del antiDiag_ht[_i+_j]
            
        return res