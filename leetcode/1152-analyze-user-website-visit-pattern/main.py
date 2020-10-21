from collections import defaultdict

"""
    1st: hashtable + recursion
    - sort the page visit records by timestamps
    - for each user, use a hashtable to record his/her page visit history
    - get all the distinct combinations(with length = 3) by each user using recursion
    - increment the page visit pattern with distinct combinations
    - find the most frequent pattern among the page visit patterns

    corner case:
    e.g. calvin: [home, about, career, abc, home, about, career, def, home, about, career]
    we count pattern "home,about,career" 1 only

    Time    O(N * nCr)
    Space   O(nCr)
    52 ms, faster than 59.65%
"""


class Solution(object):
    def mostVisitedPattern(self, usernames, timestamps, websites):
        """
        :type usernames: List[str]
        :type timestamps: List[int]
        :type websites: List[str]
        :rtype: List[str]
        """
        n = len(usernames)

        arr = []
        for i in range(n):
            arr.append((usernames[i], timestamps[i], websites[i]))
        arr = sorted(arr, key=lambda x: x[1])

        usersHistory = defaultdict(list)
        for i in range(n):
            username, _, website = arr[i]
            usersHistory[username].append(website)

        counts = defaultdict(int)

        for user in usersHistory:
            history = usersHistory[user]
            distinctPatterns = self.countOccurence(history)
            for dp in distinctPatterns:
                counts[dp] += 1

        res = ''
        maxCount = 0
        for key in counts:
            count = counts[key]
            if count > maxCount:
                res = key
                maxCount = count
            elif count == maxCount and key < res:
                res = key
        return res.split(',')

    def countOccurence(self, history):
        distinctPatterns = set()

        def dfs(candidates, chosen):
            if len(chosen) == 3:
                key = ','.join(chosen)
                distinctPatterns.add(key)
                return
            for i in range(len(candidates)):
                dfs(candidates[i+1:], chosen + [candidates[i]])
        dfs(history, [])

        return distinctPatterns


s = Solution()

a = ["joe", "joe", "joe", "james", "james",
     "james", "james", "mary", "mary", "mary"]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = ["home", "about", "career", "home", "cart",
     "maps", "home", "home", "about", "career"]
print(s.mostVisitedPattern(a, b, c))

a = ["h", "eiy", "cq", "h", "cq", "txldsscx", "cq", "txldsscx", "h", "cq", "cq"]
b = [527896567, 334462937, 517687281, 134127993, 859112386,
     159548699, 51100299, 444082139, 926837079, 317455832, 411747930]
c = ["hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi",
     "hibympufi", "hibympufi", "hibympufi", "yljmntrclw", "hibympufi", "yljmntrclw"]
print(s.mostVisitedPattern(a, b, c))
