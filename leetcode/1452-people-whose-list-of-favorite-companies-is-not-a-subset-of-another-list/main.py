"""
    1st: brute force + hashtable
    - save the favoriteCompanies as a hashtable for every person
    - for every person, find out his favoriteCompanies in a subset of another's favoriteCompanies

    Time    O(ABC)
    Space   O(A)
    1008 ms, faster than 100.00%
"""


class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        hts = []
        for i in range(len(favoriteCompanies)):
            comps = favoriteCompanies[i]
            hts.append(set(comps))
        res = []
        for i in range(len(favoriteCompanies)):
            comps = favoriteCompanies[i]
            found_ = False
            for j in range(len(hts)):
                if i == j:
                    continue
                ht = hts[j]
                found = True
                for comp in comps:
                    if comp not in ht:
                        found = False
                found_ = found_ or found

            if not found_:
                res.append(i)
        return res


"""
    2nd: brute force + hashtable
    - optimize the 1st approach with built-in hashtable substraction
    - save the favoriteCompanies as a hashtable for every person
    - for every person, find out his favoriteCompanies in a subset of another's favoriteCompanies

    pyhthon's built-in hashtable substraction
    a = set([1, 3, 5, 7, 8])
    b = set([3, 5, 7, 8, 9])
    c = set([9, 3, 5, 7, 8])
    print(a-b) <- {1}
    print(b-a) <- {9}
    print(b-c) <- {}
    print(c-b) <- {}

    Time    O(ABC)
    Space   O(A)
    1008 ms, faster than 100.00%
"""


class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        hts = []
        for i in range(len(favoriteCompanies)):
            comps = favoriteCompanies[i]
            hts.append(set(comps))
        res = []
        for i in range(len(favoriteCompanies)):
            comps = favoriteCompanies[i]
            found = False
            for j in range(len(hts)):
                if i == j:
                    continue
                remain = hts[i] - hts[j]
                if len(remain) == 0:
                    found = True
                    break
            if not found:
                res.append(i)
        return res
