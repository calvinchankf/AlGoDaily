"""
    1st: 2 arrays back and forth

    case 1:
            R _ _ _ L
    R   ->  1 2 3 4 0
    L   <-  0 4 3 2 1
            R R . L L
    
    case 2:
            R _ _ _ _ L
    R   ->  1 2 3 4 5 0
    L   <-  0 5 4 3 2 1
            R R R L L L
    
    case 3:
            _ L _ R _ _ _ L R _ _ L _ _
    R   ->  0 0 0 1 2 3 4 0 1 2 3 0 0 0
    L   <-  2 1 0 0 4 3 2 1 0 3 2 1 0 0
            L L _ R R _ L L R R L L _ _
    
    Time    O(3N)
    Space   O(2N)
    216 ms, faster than 45.31%
"""
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        Rs = n * [0]
        Ls = n * [0]
        
        cur = 0
        for i in range(n):
            if dominoes[i] == 'L':
                cur = 0
            elif dominoes[i] == 'R':
                cur = 1
            elif dominoes[i] == '.' and cur > 0:
                cur += 1
            Rs[i] = cur
        
        cur = 0
        for i in range(n-1,-1,-1):
            if dominoes[i] == 'R':
                cur = 0
            elif dominoes[i] == 'L':
                cur = 1
            elif dominoes[i] == '.' and cur > 0:
                cur += 1
            Ls[i] = cur
        # print(Rs)
        # print(Ls)
        res = ''
        for i in range(n):
            if Rs[i] > 0 and Ls[i] == 0:
                res += 'R'
            elif Rs[i] == 0 and Ls[i] > 0:
                res += 'L'
            elif Rs[i] > 0 and Ls[i] > 0:
                if Rs[i] < Ls[i]:
                    res += 'R'
                elif Rs[i] > Ls[i]:
                    res += 'L'
                else:
                    res += '.'
            else:
                res += '.'
        return res