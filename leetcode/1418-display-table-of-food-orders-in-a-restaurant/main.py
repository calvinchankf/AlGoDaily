from collections import defaultdict

"""
    1st: hastable
    - save order in hashtable, increment hashtable[(tableId, dish)] when there are another order going to the same table with the same dish
    - unpack the values when we construct the result

    [
        ["David", "3", "Ceviche"],
        ["Corina", "10", "Beef Burrito"],
        ["David", "3", "Fried Chicken"],
        ["Carla", "5", "Water"],
        ["Carla", "5", "Ceviche"],
        ["Rous", "3", "Ceviche"]
    ]

    Table, Beef Burrito, Ceviche, Fried Chicken, Water
    3       0               2       1               0
    5       0               1       0               1
    10      1               0       0               0


    Time    O(O + TlogN + DlogN + TD)
    Space   O(T + D + O)
    500 ms, faster than 100.00%
"""


class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        dishes = set()
        tables = set()

        ht = defaultdict(int)

        for _, table, dish in orders:
            dishes.add(dish)
            tableId = int(table)
            tables.add(tableId)
            ht[(tableId, dish)] += 1

        dishes = sorted(list(dishes))
        tables = sorted(list(tables))

        res = []
        res.append(["Table"] + dishes)
        for i in range(len(tables)):
            cols = []
            table = tables[i]
            cols.append(str(table))
            for dish in dishes:
                freq = ht[(table, dish)]
                cols.append(str(freq))
            res.append(cols)
        return res


s = Solution()

a = [
    ["David", "3", "Ceviche"],
    ["Corina", "10", "Beef Burrito"],
    ["David", "3", "Fried Chicken"],
    ["Carla", "5", "Water"],
    ["Carla", "5", "Ceviche"],
    ["Rous", "3", "Ceviche"]
]
print(s.displayTable(a))

a = [
    ["James", "12", "Fried Chicken"],
    ["Ratesh", "12", "Fried Chicken"],
    ["Amadeus", "12", "Fried Chicken"],
    ["Adam", "1", "Canadian Waffles"],
    ["Brianna", "1", "Canadian Waffles"]
]
print(s.displayTable(a))

a = [
    ["Laura", "2", "Bean Burrito"],
    ["Jhon", "2", "Beef Burrito"],
    ["Melissa", "2", "Soda"]
]
print(s.displayTable(a))
