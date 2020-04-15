from typing import List
from collections import defaultdict

"""
    1st: hashtable + bruteforce
    - put the transactions under each username
    - under each usernmae, check the transactions to see if there are invalid in a brutre forace manner

    Time    O(N + M^2) M: the average number of transaction under the same username
    Space   O(N)
    348 ms, faster than 23.78%
"""


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ht = defaultdict(list)
        resSet = set()
        for i in range(len(transactions)):
            t = transactions[i]
            name, time, amount, city = t.split(',')
            ht[name].append((time, amount, city, i))

        for key in ht:
            t = ht[key]
            for i in range(len(t)):
                a = t[i]
                if int(a[1]) > 1000:
                    resSet.add(a[3])
                for j in range(len(t)):
                    if i == j:
                        continue
                    b = t[j]
                    if a[2] != b[2] and abs(int(a[0]) - int(b[0])) <= 60:
                        resSet.add(a[3])
                        resSet.add(b[3])
        res = []
        for idx in resSet:
            res.append(transactions[idx])
        return res


s = Solution()

a = ["alice,20,800,mtv", "alice,50,100,beijing"]
print(s.invalidTransactions(a))

a = ["alice,20,800,mtv", "alice,50,1200,mtv"]
print(s.invalidTransactions(a))

a = ["alice,20,800,mtv", "bob,50,1200,mtv"]
print(s.invalidTransactions(a))
