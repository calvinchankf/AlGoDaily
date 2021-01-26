"""
    The first customer
    https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=669432&ctid=230591

    Write a restaurant table waiting system. Given a list of info of a diners, and K, 
    return the first customer the restaurant should serve

    e.g.
    [   
        {name: dog, size: 4, waittime: 150}, 
        {name: cat, size: 2, waittime: 200},
        {name: bird, size: 3, waittime: 300},
    ]

    if K = 3, return 'cat'
    if K = 4, return 'dog'
"""


class Customer:
    def __init__(self, name, size, waitTime):
        self.name = name
        self.size = size
        self.waitTime = waitTime


def getFirstCustomer(customers, k):
    customers.sort(key=lambda x: x.waitTime)
    for i in range(len(customers)):
        if customers[i].size <= k:
            return customers[i]
    return None


a = [
    Customer('dog', 4, 150),
    Customer('cat', 2, 200),
    Customer('bird', 3, 300),
]
b = 3
print(getFirstCustomer(a, 3).name)

a = [
    Customer('dog', 4, 150),
    Customer('cat', 2, 200),
    Customer('bird', 3, 300),
]
b = 4
print(getFirstCustomer(a, 4).name)

print("-----")

"""
    variation: The last customer
    https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=595512&ctid=230591

    e.g.
    [   
        {name: dog, size: 4, waittime: 150}, 
        {name: cat, size: 2, waittime: 200},
        {name: bird, size: 3, waittime: 300},
        {name: rat, size: 7, waittime: 400},
    ]

    if K = 3, return 'cat'
    if K = 5, return 'rat'
"""


def getFirstCustomer(customers, k):
    res = None
    customers.sort(key=lambda x: x.waitTime)
    for i in range(len(customers)):
        if customers[i].size <= k:
            res = customers[i]
    return res


a = [
    Customer('dog', 4, 150),
    Customer('cat', 2, 200),
    Customer('bird', 3, 300),
    Customer('rat', 7, 400),
]
b = 3
print(getFirstCustomer(a, 3).name)

a = [
    Customer('dog', 4, 150),
    Customer('cat', 2, 200),
    Customer('bird', 3, 300),
    Customer('rat', 4, 700),
]
b = 4
print(getFirstCustomer(a, 4).name)
